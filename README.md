# 🤖 AI-Powered Data Analysis Chat

An intelligent data analysis platform that allows you to chat with your CSV data using natural language, powered by Google Gemini AI and LangChain.

![AI Data Chat](https://img.shields.io/badge/AI-Powered-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) ![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)

## ✨ Features

### 💬 ChatGPT-Style Interface
- **Natural Language Queries**: Ask questions in plain English
- **Instant Responses**: Get answers and visualizations immediately
- **Persistent Chat History**: Keep track of your analysis conversation
- **Inline Visualizations**: Plots appear directly in the chat

### 📊 Comprehensive Data Overview
- **Dataset Preview**: View your entire dataset in an interactive table
- **Statistical Summary**: Automatic descriptive statistics
- **Data Quality Reports**: Missing values, duplicates, and completeness metrics
- **Column Distributions**: Interactive histograms and box plots

### 📈 Smart Visualizations
- **Correlation Heatmaps**: Understand relationships between variables
- **Scatter Plots**: Explore variable relationships
- **Bar Charts**: Visualize categorical distributions
- **Custom Visualizations**: Request any chart through natural language

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- Google Gemini API key

### Installation

1. **Clone or download this repository**

2. **Install uv** (if not already installed):
   ```bash
   pip install uv
   ```

3. **Initialize uv project** (if starting fresh):
   ```bash
   uv init
   ```

4. **Install all dependencies from pyproject.toml**:
   ```bash
   uv sync
   ```
   
   Or to add dependencies individually:
   ```bash
   uv add streamlit pandas matplotlib seaborn langchain langchain-experimental langchain-google-genai python-dotenv
   ```

5. **Set up your API key**:
   
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   ```
   
   Get your API key from: https://makersuite.google.com/app/apikey

6. **Run the application**:
   ```bash
   uv run streamlit run main.py
   ```

The app will open automatically at `http://localhost:8501`

## 📖 How to Use

### 1. Upload Your Data
- Click "Upload CSV" in the sidebar
- Select your CSV file
- Wait for "✅ Ready!" message

### 2. Navigate Between Pages
Use the navigation bar at the top:
- **💬 Chat with Data**: Ask questions about your data
- **📊 Data Overview**: Explore statistics and data quality
- **📈 Visualizations**: Generate custom charts

### 3. Chat with Your Data

**Example Questions:**
```
How many records are in the dataset?
Show me a histogram of the age column
What is the correlation between price and quantity?
Create a scatter plot of X vs Y
Show me missing values by column
What is the average value of sales by region?
```

### 4. Explore Data Overview

Navigate through tabs:
- **Preview**: See your raw data
- **Statistics**: View descriptive statistics
- **Quality**: Check data completeness
- **Distribution**: Explore column distributions

### 5. Create Visualizations

Choose from:
- Correlation Heatmap
- Scatter Plot
- Bar Chart
- Custom Query (describe what you want!)

## 🎯 Use Cases

- **Business Analytics**: Analyze sales, revenue, customer data
- **Research**: Explore datasets, find patterns, test hypotheses
- **Education**: Learn data analysis interactively
- **Data Exploration**: Quick insights before deep analysis

## 💡 Example Workflow

1. Upload `titanic.csv` (included in the repo)
2. Ask: "How many passengers survived?"
3. Ask: "Show me a histogram of ages"
4. Navigate to Visualizations
5. Create a correlation heatmap
6. Go to Data Overview to check data quality

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI/LLM**: Google Gemini 2.0 Flash via LangChain
- **Data Analysis**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Environment**: Python-dotenv

## 📁 Project Structure

```
data_analysis_app/
├── main.py                 # Main Streamlit application
├── .env                    # API keys (create this)
├── requirements.txt        # Python dependencies
├── pyproject.toml         # Project configuration
├── titanic.csv            # Sample dataset
└── README.md              # This file
```

## 🎨 Screenshots

### Chat Interface
Ask questions and get instant answers with visualizations:

```
User: Show me a histogram of ages
AI: [Displays histogram] Here's the distribution of ages in your dataset...
```

### Data Overview
Comprehensive statistics and data quality metrics in organized tabs.

### Visualizations
Generate custom charts through dropdown menus or natural language queries.

## 🔧 Configuration

### Customize Gemini Model

Edit `main.py` line 36:
```python
ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0)
```

Available models:
- `gemini-2.0-flash-exp` (default, fast)
- `gemini-pro`
- `gemini-pro-vision`

### Adjust Sidebar Width

Edit CSS in `main.py` around line 17:
```css
min-width: 350px;  /* Change this value */
max-width: 350px;
```

## 🐛 Troubleshooting

### "API key not found"
- Ensure `.env` file exists in project root
- Check that `GOOGLE_API_KEY` is set correctly
- Restart the Streamlit app

### "Module not found"
```bash
uv pip install -r requirements.txt
```

### Plots not displaying
- Make sure you're asking for specific visualization types
- Try: "Create a histogram" instead of "Show me data"

### Agent errors
- Ensure your CSV has proper headers
- Check for data type issues
- Try simpler queries first

## 📝 Dependencies

Main packages:
- `streamlit` - Web interface
- `pandas` - Data manipulation
- `langchain` - LLM framework
- `langchain-google-genai` - Gemini integration
- `matplotlib` - Plotting
- `seaborn` - Statistical visualizations

See `requirements.txt` for complete list.

## 🔐 Security Notes

- Never commit your `.env` file
- Keep API keys private
- The `.gitignore` file excludes `.env` automatically
- Use environment variables for production deployment

## 🚀 Deployment

### Streamlit Cloud

1. Push code to GitHub (without `.env`)
2. Go to streamlit.io/cloud
3. Connect repository
4. Add `GOOGLE_API_KEY` in Secrets
5. Deploy!

### Local Production

```bash
uv run streamlit run main.py --server.port 8080
```

## 🤝 Contributing

Suggestions and improvements welcome! Areas for enhancement:
- Support for Excel files
- Database connectivity
- Export analysis results
- More visualization types
- Multi-language support

## 📄 License

This project is open-source and available for educational purposes.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini](https://deepmind.google/technologies/gemini/)
- LangChain for LLM orchestration

## 📧 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review Google Gemini documentation
3. Check Streamlit documentation

---

**Made with ❤️ using Streamlit and Google Gemini AI**

🌟 Star this repo if you find it useful!