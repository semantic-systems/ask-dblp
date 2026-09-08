
# [ASK-DBLP](https://ceur-ws.org/Vol-4085/paper76.pdf): A natural language interface for DBLP KG.
This work is presented as a demo work at ISWC 2025, Nara, Japan. The paper can be found [here](https://ceur-ws.org/Vol-4085/paper76.pdf).
## How  to run

Run this project by simply following the instructions:

```bash
# clone the repository
# create virtual environment
# activate virtual environment
pip install -r requirements.txt

cp .env-example .env
```

Modify the `.env` file and ad your keys and variables there. Then run the app:

```
python app.py
```

Go to the root directory of your Next.js project.
Create a file named .env.local (if it doesn't already exist).
Add your environment variable, for example: `API_URL=http://127.0.0.1:5000` and save the file.

Open another Terminal:

```
cd dblp-nli-app
npm run dev
```

Then, you can now view the DBLP SPARQL generation app in your browser at `http://localhost:3000`.
