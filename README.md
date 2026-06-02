# Saleasy

Un assistant commercial complet dans Claude. A complete sales assistant inside Claude.

Saleasy t'accompagne sur toute la vie d'une vente: attirer, prospecter, vendre et fidéliser. Tu l'installes une fois, tu réponds à quelques questions sur ton activité, puis tu lui parles normalement. Il fait le travail et s'adapte à ton métier, ton offre et ton style.

---

## Français

### En clair
Tu dis ce dont tu as besoin ("prépare mon rendez-vous de demain", "écris une relance pour ce prospect", "trouve 20 prospects dans le secteur X") et Saleasy s'en occupe. Pas de configuration technique, pas de clé à coller. Un court entretien au départ et c'est parti.

Ce n'est pas un simple gadget. Derrière quatre commandes se cache une vraie bibliothèque de méthodes commerciales (prospection, copywriting, closing, négociation, prévisions, fidélisation). Claude charge la bonne méthode au bon moment, sans que tu aies à la chercher.

### Ce que Saleasy fait pour toi

#### 1. Configuration (une seule fois)
Un court entretien sur ton marché, ton offre, ta cible, ton ton et tes outils. Saleasy garde ce profil et l'utilise partout, donc tu n'as plus jamais à tout réexpliquer. Tu peux le modifier quand tu veux.

#### 2. Marketing et visibilité
Posts LinkedIn, optimisation de ton profil LinkedIn, calendrier de contenu, campagnes, articles de blog, pages de vente, newsletters, référencement Google (SEO), recyclage d'un contenu en plusieurs formats, lead magnets et positionnement. Chaque contenu vise une douleur client précise et s'appuie sur tes preuves (cas clients, chiffres), jamais sur des promesses inventées.

#### 3. Prospection
Remplir et travailler le haut du tunnel. Concrètement, Saleasy sait:

- construire une liste de prospects propre et notée (du plus chaud au plus froid), dans le respect du RGPD.
- repérer le bon moment pour contacter (levée de fonds, recrutement, changement de direction).
- écrire un cold email court ou une séquence de relance (J0, J3, J7, J10), avec un contrôle qualité avant de te montrer quoi que ce soit.
- surveiller des comptes en continu et te prévenir dès qu'un signal apparaît.
- envoyer les messages que tu as validés, via ta messagerie officielle, puis noter le résultat.

#### 4. Vente et fidélisation
Du premier rendez-vous à la signature et après:

- préparer un rendez-vous (fiche synthèse) ou transformer tes notes d'appel en actions et en email de suivi.
- faire le point sur ton pipeline et bâtir une prévision (forecast) honnête.
- t'aider à closer et à négocier sans brader (objections, échelle de concessions, jeux d'acteurs).
- rédiger une proposition en trois offres (Bon, Mieux, Meilleur) avec un calcul de retour sur investissement.
- faire grandir tes comptes clients (montée en gamme, risque de non-renouvellement, recommandations).
- un brief le matin et un bilan chaque semaine pour piloter.

### Sécurité et respect des règles
Saleasy n'envoie jamais rien sans ton accord. Claude rédige, tu valides, Claude envoie via tes outils officiels (Gmail ou Microsoft 365), puis note le résultat. Il reste dans les règles des plateformes: aucune automatisation cachée de LinkedIn, aucun contournement des protections. Les données de contact viennent de sources autorisées et publiques, dans le respect du RGPD.

### Tes fichiers
Saleasy crée deux fichiers dans ton dossier de travail, jamais publiés:

- ton profil (marché, offre, cible, ton, outils).
- ton suivi de prospects et d'affaires. Si tu as un CRM connecté, le CRM fait foi et ce fichier le recopie.

### Installation
Colle ces deux lignes dans Claude:

```
/plugin marketplace add MariusYvard/saleasy
/plugin install saleasy@saleasy
```

Aucune clé, aucun réglage technique. Ensuite, dis "configure saleasy" pour démarrer. Saleasy fonctionne seul avec la recherche web et devient plus efficace si tu connectes tes outils: email, agenda, CRM, base de prospects, réseau social, tableur. Voir `CONNECTORS.md`.

---

## English

Saleasy is a complete sales assistant inside Claude. Install it once, answer a few questions about your business, then let it help at every stage of a deal: attract, prospect, sell and grow accounts. You talk to it in plain language ("prepare my meeting tomorrow", "write a follow-up to this prospect") and it adapts to your job, your offer and your style.

It is not a small gadget. Behind four commands sits a real library of sales methods (prospecting, copywriting, closing, negotiation, forecasting, retention). Claude loads the right method at the right moment so you never have to look it up.

### What it does for you

- Set up once with a short interview about your market, offer, target, tone and tools, kept in a profile and reused everywhere.
- Create marketing: LinkedIn posts and profile, content calendar, campaigns, blog and landing pages, newsletters, SEO, repurposing, lead magnets and positioning.
- Run prospecting end to end: build a clean scored list under GDPR, spot the moment to reach out, write cold emails or a J0/J3/J7/J10 sequence, watch accounts for signals and send what you approved from your own mailbox.
- Handle selling from first meeting to renewal: meeting prep and call summaries, pipeline review and an honest forecast, closing and negotiation without discounting, three-tier proposals with an ROI case, account growth and a daily brief with a weekly review.

### Safety
Saleasy never sends anything without your yes. Claude drafts, you approve, Claude sends through your official tools (Gmail or Microsoft 365), then logs the result. It stays within platform rules: no hidden LinkedIn automation, no bypass of protections. Contact data comes from authorized public sources under GDPR.

### Install
Paste these two lines into Claude:

```
/plugin marketplace add MariusYvard/saleasy
/plugin install saleasy@saleasy
```

No keys, no technical setup. Then say "configure saleasy" to start. Saleasy works on its own with web search and gets stronger when you connect email, calendar, CRM, lead data, social or a spreadsheet. See `CONNECTORS.md`.

---

## For developers
This repository is a Claude plugin marketplace with four skills and twelve reference playbooks. A house-style linter (`scripts/lint-skills.py`) runs in GitHub Actions on every push and pull request. It rejects a comma before "and" or "or", a banned marketing superlative and a malformed skill description. See `CONTRIBUTING.md`. Licensed MIT.
