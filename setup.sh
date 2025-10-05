mkdir -p ~/.streamlit/
echo "\
[server]\n\nheadless = true\nport = $PORT\nenableCORS = false\n\n\n" > ~/.streamlit/config.toml
