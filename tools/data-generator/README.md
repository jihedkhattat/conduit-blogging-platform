# Test data generator

Python scripts written in milestone 1 to fill a fresh Conduit backend with realistic test data
through the public REST API (no direct database access):

| Script | What it does |
|---|---|
| `create_users.py` | Registers 20 users and stores their JWT tokens in `test_tokens.txt` |
| `create_articles.py` | Creates 200 Markdown articles (3–4 tags each) with random authors |
| `like_articles.py` | Likes 50 random articles 1–5 times each |
| `kommentare.py` | Adds 1–3 comments to 20 random articles |
| `follow.py` | Lets 5 users follow 1–3 other users |

## Usage

Start the API first (see the main README), then:

```bash
cd tools/data-generator
pip install -r requirements.txt
python create_users.py
python create_articles.py
python like_articles.py
python kommentare.py
python follow.py
```

The scripts talk to `http://localhost:8081/api`. Change `API_BASE` at the top of each script if
your backend runs elsewhere.
