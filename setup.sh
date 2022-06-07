mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
\n\
[theme]\n\
primaryColor=\"#002171\"\n\
backgroundColor=\"#F1F1F1\"\n\
secondaryBackgroundColor=\"#FFFFFF\"\n\
textColor=\"#262730\"\n\
font=\"sans serif\"\n\
\n\
" > ~/.streamlit/config.toml