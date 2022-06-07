mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
primaryColor=\"\#002171\"\n\
backgroundColor=\"\#F1F1F1\"\n\
\n\
" > ~/.streamlit/config.toml