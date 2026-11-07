# Start a simple Python driven web server
# Expose the current directory static files and its subdirectories to the web
# on port 8080
python3 -m http.server 8080

# Setting the bind address to 127.0.0.1 / 0.0.0.0
python3 -m http.server 8080 --bind 127.0.0.1
python3 -m http.server 8080 --bind 0.0.0.0































