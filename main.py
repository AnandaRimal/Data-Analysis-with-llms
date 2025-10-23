import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(page_title="AI Data Analysis", layout="wide", page_icon="🤖", initial_sidebar_state="expanded")

# Custom CSS for wider sidebar and navigation bar
st.markdown("""
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] {
        min-width: 350px;
        max-width: 350px;
    }
    .nav-bar {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .nav-bar h2 {
        color: white;
        margin: 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = None
if 'agent' not in st.session_state:
    st.session_state.agent = None
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Chat"

# Sidebar
with st.sidebar:
    st.title("🤖 AI Data Chat")
    st.markdown("---")
    
    uploaded_file = st.file_uploader("📁 Upload CSV", type=["csv"])
    
    if uploaded_file is not None and st.session_state.df is None:
        st.session_state.df = pd.read_csv(uploaded_file)
        
        with st.spinner("Creating AI agent..."):
            st.session_state.agent = create_pandas_dataframe_agent(
                ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0),
                st.session_state.df,
                verbose=True,
                allow_dangerous_code=True
            )
    
    if st.session_state.df is not None:
        st.success("✅ Ready!")
        st.markdown("---")
        st.info(f"**{st.session_state.df.shape[0]}** rows × **{st.session_state.df.shape[1]}** columns")
        
        st.markdown("---")
        
        if st.button("� Reset", use_container_width=True):
            st.session_state.df = None
            st.session_state.agent = None
            st.session_state.messages = []
            st.session_state.current_page = "Chat"
            st.rerun()

# Navigation Bar at top
if st.session_state.df is not None:
    st.markdown('<div class="nav-bar"><h2>📊 AI Data Analysis Platform</h2></div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns([3, 3, 3, 3])
    
    with col1:
        if st.button("� Chat with Data", use_container_width=True, type="primary" if st.session_state.current_page == "Chat" else "secondary"):
            st.session_state.current_page = "Chat"
            st.rerun()
    
    with col2:
        if st.button("� Data Overview", use_container_width=True, type="primary" if st.session_state.current_page == "Overview" else "secondary"):
            st.session_state.current_page = "Overview"
            st.rerun()
    
    with col3:
        if st.button("� Visualizations", use_container_width=True, type="primary" if st.session_state.current_page == "Visualizations" else "secondary"):
            st.session_state.current_page = "Visualizations"
            st.rerun()
    
    st.markdown("---")

# Main content
if st.session_state.df is None:
    st.title("🤖 AI-Powered Data Analysis")
    st.markdown("### Upload a CSV file to start")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 💬 Chat\nAsk questions naturally")
    with col2:
        st.markdown("### 📊 Overview\nExplore your data")
    with col3:
        st.markdown("### 📈 Visuals\nGenerate charts")

else:
    df = st.session_state.df
    
    # CHAT PAGE - ChatGPT style
    if st.session_state.current_page == "Chat":
        st.title("💬 Chat with Your Data")
        
        with st.expander("💡 Example Questions"):
            st.markdown("- How many records are there?\n- Show histogram of age\n- Correlation between X and Y?")
        
        st.markdown("---")
        
        # Display chat history
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
                if msg.get("figure"):
                    st.pyplot(msg["figure"])
        
        # Chat input
        if prompt := st.chat_input("Ask anything..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        plt.close('all')
                        response = st.session_state.agent.run(prompt)
                        
                        has_plots = len(plt.get_fignums()) > 0
                        figures = []
                        
                        if has_plots:
                            for fig_num in plt.get_fignums():
                                fig = plt.figure(fig_num)
                                figures.append(fig)
                                st.pyplot(fig)
                        
                        st.markdown(response)
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": response,
                            "figure": figures[0] if figures else None
                        })
                        plt.close('all')
                        
                    except Exception as e:
                        error_msg = f"Error: {str(e)}"
                        st.error(error_msg)
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})
    
    # DATA OVERVIEW PAGE
    elif st.session_state.current_page == "Overview":
        st.title("📊 Data Overview")
        
        tab1, tab2, tab3, tab4 = st.tabs(["📋 Preview", "📈 Statistics", "🔍 Quality", "📊 Distribution"])
        
        with tab1:
            st.subheader("Dataset Preview")
            st.dataframe(df, use_container_width=True, height=400)
        
        with tab2:
            st.subheader("Statistical Summary")
            st.dataframe(df.describe(), use_container_width=True)
            
            st.subheader("Column Info")
            col_info = pd.DataFrame({
                'Column': df.columns,
                'Type': df.dtypes.astype(str),
                'Non-Null': df.count(),
                'Unique': df.nunique()
            })
            st.dataframe(col_info, use_container_width=True)
        
        with tab3:
            st.subheader("Data Quality")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Rows", df.shape[0])
                st.metric("Columns", df.shape[1])
                st.metric("Duplicates", df.duplicated().sum())
            with col2:
                missing = df.isnull().sum().sum()
                st.metric("Missing Values", missing)
                st.metric("Complete Rows", df.dropna().shape[0])
                st.metric("Memory", f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
            
            if missing > 0:
                st.subheader("Missing by Column")
                missing_df = pd.DataFrame({
                    'Column': df.columns,
                    'Missing': df.isnull().sum(),
                    '%': (df.isnull().sum() / len(df) * 100).round(2)
                })
                missing_df = missing_df[missing_df['Missing'] > 0].sort_values('Missing', ascending=False)
                st.dataframe(missing_df, use_container_width=True)
        
        with tab4:
            st.subheader("Column Distributions")
            
            numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
            if numeric_cols:
                col = st.selectbox("Select column:", numeric_cols)
                
                c1, c2 = st.columns(2)
                with c1:
                    fig, ax = plt.subplots(figsize=(8, 5))
                    df[col].hist(bins=30, ax=ax, edgecolor='black')
                    ax.set_title(f'Distribution of {col}')
                    st.pyplot(fig)
                    plt.close()
                
                with c2:
                    fig, ax = plt.subplots(figsize=(8, 5))
                    df.boxplot(column=col, ax=ax)
                    ax.set_title(f'Box Plot of {col}')
                    st.pyplot(fig)
                    plt.close()
    
    # VISUALIZATIONS PAGE
    elif st.session_state.current_page == "Visualizations":
        st.title("📈 Visualizations")
        
        viz_type = st.selectbox("Visualization Type:", ["Correlation Heatmap", "Scatter Plot", "Bar Chart", "Custom Query"])
        
        if viz_type == "Correlation Heatmap":
            numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
            if len(numeric_cols) > 1:
                fig, ax = plt.subplots(figsize=(12, 8))
                correlation = df[numeric_cols].corr()
                sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', center=0, ax=ax)
                ax.set_title('Correlation Heatmap')
                st.pyplot(fig)
                plt.close()
            else:
                st.warning("Need more numeric columns")
        
        elif viz_type == "Scatter Plot":
            numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
            if len(numeric_cols) >= 2:
                c1, c2 = st.columns(2)
                with c1:
                    x_col = st.selectbox("X-axis:", numeric_cols)
                with c2:
                    y_col = st.selectbox("Y-axis:", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
                
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.scatter(df[x_col], df[y_col], alpha=0.6)
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                ax.set_title(f'{x_col} vs {y_col}')
                ax.grid(True, alpha=0.3)
                st.pyplot(fig)
                plt.close()
        
        elif viz_type == "Bar Chart":
            categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
            if categorical_cols:
                col = st.selectbox("Column:", categorical_cols)
                
                value_counts = df[col].value_counts().head(10)
                fig, ax = plt.subplots(figsize=(10, 6))
                value_counts.plot(kind='bar', ax=ax, color='steelblue')
                ax.set_title(f'Distribution of {col}')
                plt.xticks(rotation=45, ha='right')
                st.pyplot(fig)
                plt.close()
        
        elif viz_type == "Custom Query":
            st.subheader("Custom Visualization")
            query = st.text_area("Describe visualization:", placeholder="e.g., KDE plot for column X")
            
            if st.button("Generate", type="primary"):
                if query and st.session_state.agent:
                    with st.spinner("Creating..."):
                        try:
                            plt.close('all')
                            response = st.session_state.agent.run(query)
                            
                            if len(plt.get_fignums()) > 0:
                                for fig_num in plt.get_fignums():
                                    st.pyplot(plt.figure(fig_num))
                            
                            st.success(response)
                            plt.close('all')
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
