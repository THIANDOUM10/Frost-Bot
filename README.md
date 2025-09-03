





# ❄️ Frost Bot

<p align="center">
  <img src="https://files.catbox.moe/xhtqm5.png" alt="Thumbnail" />
</p>

````markdown
---

## 🤖 Présentation
**Frost Bot** est un bot Discord développé par **KINGFROST** pour profiter pleinement de Discord 🚀.  
Il allie **fun**, **jeux**, **interactions sociales**, et **outils de modération** dans une expérience fluide et stylisée ❄️.

---

## ✨ Fonctionnalités principales

### 🎮 Fun & Jeux
- `!dice` → lancer un dé 🎲  
- `!roll <faces>` → lancer un dé personnalisé  
- `!8ball <question>` → boule magique 🔮  
- `!coinflip` → pile ou face 🪙  
- `!meme` → envoie un meme aléatoire 😂  
- `!pendu` + `!guesspendu` → jeu du pendu multijoueur 🎮  
- `!rps` → pierre-papier-ciseaux ✊✋✌️  

### 🤺 Interactions
- `!hug @user` → câlin 🤗  
- `!kiss @user` → bisou 😘  
- `!slap @user` → claque 👋  
- `!fight @user` → duel ⚔️  
- `!love @user1 @user2` → compatibilité amoureuse ❤️  
- `!ship @user1 @user2` → crée un ship name 💘  

### 🛠️ Modération
- `!kick @user` → expulse un membre 🚪  
- `!ban @user` → bannit un membre 🔨  
- `!clear <nombre>` → supprime des messages 🧹  
- `!mute / !unmute` → gérer les mutes ⏳  
- `!warn / !warnings` → avertir les membres ⚠️  

### ℹ️ Infos & Utilitaires
- `!ping` → latence du bot 🏓  
- `!uptime` → depuis combien de temps Frost Bot tourne ⏳  
- `!botinfo` → infos sur Frost Bot ❄️  
- `!menu` → menu interactif avec toutes les commandes 📜  


````
## 🚀 Installation

1. Clone le dépôt :

   ```bash
   git clone https://github.com/TON-USER/Frost-Bot.git
   cd Frost-Bot


2. Crée un environnement virtuel et installe les dépendances :

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate      # Windows

   pip install -r requirements.txt
   ```

3. Configure ton **token Discord** dans un fichier `.env` :

   ```env
   DISCORD_TOKEN=ton_token_ici
   ```

4. Lance le bot :

   ```bash
   python start.py
   ```

---

## 📦 Structure du projet

```
Frost-Bot/
│── cogs/
│   ├── fun.py         # Commandes fun & jeux
│   ├── moderator.py   # Commandes de modération
│   ├── menu.py        # Menu interactif
│   ├── info.py        # Ping, uptime, botinfo
│── start.py           # Fichier principal
│── requirements.txt   # Dépendances
│── README.md          # Documentation
│── .env.example       # Exemple de configuration
```

---

## 🔐 Sécurité

⚠️ **Ne mets jamais ton token Discord en clair dans `start.py` ni dans ton repo GitHub.**
Utilise un fichier `.env` (comme montré ci-dessus). Tu peux inclure un fichier `.env.example` pour montrer la structure sans exposer ton vrai token.

---

## 👑 Auteur

Développé par **KINGFROST**
⭐ N’hésite pas à donner une étoile au repo si Frost Bot t’a plu !


