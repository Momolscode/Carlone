# Intégration ChatGPT — 4 novembre 2026

Cet index accompagne les pièces retrouvées dans la conversation de Morgan sur Carlone. Il complète le dépôt existant sans remplacer les décisions et documents des autres conversations.

## Lire en premier

1. [Contexte du dossier existant](../interne/contexte-projet-carlone.md).
2. [Complément et limites des nouvelles sources](../interne/complement-chatgpt-2026-11-04.md).
3. [Inventaire technique et provenance](inventaire-integration-chatgpt-2026-11-04.json).

**Le dépôt est privé.** `interne/` contient des rémunérations, stratégies de négociation, budgets et scénarios historiques : ne pas remettre ce dossier au client. `pour-carlone/` regroupe des supports de présentation ; ce classement n'atteste pas leur validation ni leur envoi.

## Pièces ajoutées

| Sujet | Pièces | État |
| --- | --- | --- |
| Éclosion | [Concept PDF](../pour-carlone/eclosion/concept-2026-10-31.pdf), [visuel](../pour-carlone/eclosion/visuel-fleur-cinetique.png), [animation 1080p](../pour-carlone/eclosion/animation-concept-1080p-2026-10-31.mp4) | Intention artistique ; aucune construction ou recette attestée |
| Prototype Éclosion P0 | [Étude mécanique](../interne/eclosion/ebauche-mecanique-p0-2026-10-31.pdf), [archive originale](../interne/eclosion/sources-p0-2026-10-31.zip), [sources CAO extraites](../interne/eclosion/prototype-p0/), [master vidéo archivé en parties](../interne/eclosion/medias-source/) | Prototype numérique ; fichiers extraits sans exécution du script |
| STRATES | [Concept vidéo IA de 10 secondes](../pour-carlone/strates/bras-robotique-concept-ia-10s.mp4), [relief en galerie](../pour-carlone/strates/relief-mineral-bleu-galerie.png) | Visualisations conceptuelles ; pas une démonstration de robot réel |
| Laboratoire | [Audit du 31 octobre](../interne/laboratoire/audit-ia-robotique-2026-10-31.pdf), [visuels](../pour-carlone/laboratoire-ia-robotique/visuels/) | Étude et intentions, financement non validé |
| Structure et rémunération | [Étude du 29 octobre](../interne/archives-marwin-tech/choix-structure-2026-10-29.pdf), [options v5 du 30 octobre](../interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf) | Archives internes ; hypothèses juridiques, sociales et fiscales à réexaminer avant usage |
| Peinture robotique | [Dossier investisseur v1](../interne/strates/archives-investisseur/dossier-investisseur-v1-2026-11-02.pdf), [budget modifiable](../interne/strates/archives-investisseur/budget-v1-2026-11-02.xlsx) | Ancien scénario R&D ; ne remplace pas STRATES phase 1 |
| Pages de contexte | [Offres et projets](chatgpt-pages/2026-11-04/carlone-offres-et-projets.md), [accompagnement](chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md) | Copies des pages lues le 4 novembre ; blocs JSON conservés à côté |
| CRM | [Référence du dépôt et de la branche](crm-reference-2026-11-04.md) | Code et données conservés dans leur dépôt canonique |

La proposition STRATES du 2 novembre et son audit robotique étaient déjà présents, avec les mêmes empreintes : ils n'ont pas été dupliqués.

## Limites de récupération

Quatre références d'images ont été retrouvées mais leurs fichiers binaires n'ont pas pu être récupérés :
- Atelier MARWIN TECH, art et robotique ;
- Bras robotique éducatif au cube rouge ;
- Rivière ultramarine dans la pierre ;
- Bras robotique peignant un relief fluvial bleu.

Leurs identifiants figurent dans l'inventaire. Les documents en ligne non exportables déjà signalés dans le README restent également hors de cette intégration. Aucun avancement opérationnel n'est déduit de cet archivage.


## Fichiers volumineux

La limite de transfert impose deux conditionnements sans perte : le PDF v5 est allégé par suppression de l’enveloppe ASCII85 de ses images (texte et pixels décodés contrôlés identiques) ; son fichier original exact est conservé en `.original.pdf.gz`. Le master vidéo est réparti en trois parties binaires ; le MP4 1080p reste directement utilisable. Le [script de restitution](../tools/restaurer-archives.py) reconstitue et contrôle les originaux dans un dossier de sortie choisi, sans écraser les fichiers existants.

## Reprise des visuels manquants

La [reprise des 59 lectures et des visuels](reprise-59-et-visuels-2026-11-04.md) ajoute trois versions incorporées aux PDF (relief bleu, bras peintre et bras éducatif). Les quatre fichiers Library originaux restent non vérifiés ; ces extractions sont explicitement distinguées des originaux.
