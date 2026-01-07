const express = require("express");
const cors = require("cors");
const db = require("./database");

const app = express();

app.use(cors());
app.use(express.json());

app.get("/usuarios", (req, res) => {
  db.all("SELECT id, nome, email FROM usuarios", [], (err, rows) => {
    if (err) {
      return res.status(500).json(err);
    }
    res.json(rows);
  });
});

app.post("/usuarios", (req, res) => {
  const { nome, email, senha } = req.body;

  const sql = `
    INSERT INTO usuarios (nome, email, senha)
    VALUES (?, ?, ?)
  `;

  db.run(sql, [nome, email, senha], function (err) {
    if (err) {
      return res.status(400).json({ error: err.message });
    }
    res.json({ id: this.lastID });
  });
});

app.listen(3000, () => {
  console.log("Servidor rodando em http://localhost:3000");
});
