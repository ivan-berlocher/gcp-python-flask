# F:Core 플랫폼 Architecture

## 1. Purpose and Scope

Ce document présente une plateforme low-code/no-code permettant de créer, configurer et déployer des agents et outils IA pour divers domaines (collecte de données, analyse, conversation, services métiers verticaux).

Principales composantes :

- **MCP Server** : gestion centralisée du contexte de session, prompts dynamiques et routage multimodal (texte, audio, vision) avec fragmentation/summarisation.
- **Agent Framework** : orchestrations ReAct, Plan-and-Execute, Chain-of-Thought, Function-Calling et Sequential Thinking.
- **Low-Code Workflow Builder** : interface visuelle React Flow pour composer les agents et tools avec exécution en un clic et monitoring en temps réel.
- **Developer Studio** : éditeur Monaco intégré pour coder, tester et publier des Tools/Agents dans un sandbox.

La solution vise des cas d'usage métiers allant de la gestion de projets de construction (F:Core) à l'éducation (Tutor/LMS) et tout autre scénario nécessitant des agents IA modulaires.

## 2. F:Core 플랫폼 Architecture Overview

### 2.1 Collecte des données
- **시공사 데이터** : données des entreprises de construction
- **협력 업체 데이터** : données des sous-traitants
- **입찰 데이터** : appels d'offres
- **낙찰 데이터** : adjudications
- **공사 데이터** : suivi de chantier

### 2.2 Cœur de la plateforme
- **F:Collector** : Source Connector, Ingestion Scheduler, Content Parser, Data Normalizer, Metadata Extractor, Storage Adapter
- **F:Insight** : Classification, Embedding Generator, Résumé de documents, Topic Analysis, NER, Sentiment Analysis, Détection d'anomalies, Prévision
- **F:Assistant** : Prétraitement (Tokenizer, Intent Classifier, Entity Tagger), Prompt Builder, LLM Execution (Router, Adapter, Rate Limiter), Post-processing (Fact-check, Validation), Session Memory, STT/TTS, Cache audio

### 2.3 Services métiers spécifiques
- Automatisation chantiers : présence QR, calculs de règlements, génération de contrats
- Analyse d'appels d'offres : matching, scoring, géolocalisation
- Estimation ressources : main-d'œuvre, matériel
- Recommandation et notification de sous-traitants

### 2.4 Interfaces utilisateur
- Utilisateurs finaux : portail terrain (QR, chat, formulaires)
- Administrateurs : back-office complet (tableaux de bord, configuration, supervision)

### 2.5 Circuit de données global
F:Collector → Stockage/normalisation → F:Insight → API Gate → F:Assistant → UI Web

## 3. Key Objectives
- Faciliter la composition et le déploiement de workflows IA pour des profils non-tech
- Offrir un studio de développement en ligne pour coder, tester et publier des tools et agents
- Garantir une mémoire de session robuste et un routage dynamique des modèles
- Supporter les principales stratégies de raisonnement IA et la sélection automatique par le LLM
- Proposer un catalogue riche de tools et agents préconstruits
- Intégrer des workflows verticaux (ex. F:Core) en low-code

## 4. Functional Requirements
- Low-Code Workflow Builder : palette dynamique, canvas React Flow, formulaires JSON Schema, exécution et logs via WebSocket
- Developer Studio : éditeur Monaco, structure de projet, exécutions sandbox, tests unitaires, publication versionnée
- MCP Server & Memory : endpoints `GET/POST /context`, registre de tools, endpoint de résumé, stockage Redis + Postgres+pgvector, support multimodal
- Orchestration d'agents et sélection de stratégie : ReAct, Plan-and-Execute, CoT, Function-Calling, Sequential Thinking
- Récupération sémantique de tools ou filtrage par catégorie
- Boucle jusqu'à réponse finale ou complétion de branche
- Modules préconstruits : DataOps, Analytics, Conversational, Tutor/LMS, Sequential Thinking
- Workflows spécifiques au domaine : modules F:Core et templates construction

## 5. Exemple d'exécution
```json
{
  "query": "Quel est le solde total des fournisseurs du secteur A ?",
  "context": {"userId": "U123", "lastQuery": "secteur A"}
}
```
Trace typique :
1. `intent_classifier` → `{ "intent": "get_balance" }`
2. `retrieve_context` → contexte pertinent (dernier solde connu, date)
3. `prompt_builder` → prompt complet pour LLM
4. `call_llm` → "Le solde total est de 1 234 567 €"
5. `fact_check` → validation via requête SQL

Réponse :
```json
{
  "responseText": "Le solde total des fournisseurs du secteur A est de 1 234 567 €.",
  "usedTools": ["intent_classifier", "retrieve_context", "prompt_builder", "call_llm", "fact_check"],
  "timestamp": "2025-06-10T14:30:00Z"
}
```

## Cha\u00eene de traitement

La configuration cr\u00e9\u00e9e dans le **Frontend Low\u2011Code Builder** est envoy\u00e9e vers l'API \
qui transmet au **MCP Server / Memory**. Ce dernier orchestre l'ex\u00e9cution en \
s'appuyant sur les **Agno Core Agents ou LangChain Agents** qui pilotent les \
tools n\u00e9cessaires.

## Pile technologique recommand\u00e9e

| Couche | Technologies recommand\u00e9es |
| ------ | ---------------------------- |
| UI graphique | React.js + Next.js |
| Canvas | React Flow |
| Design system | Tailwind CSS + shadcn/ui |
| Formulaires | @rjsf/core |
| State client | Zustand ou Recoil |
| Data‑fetching | TanStack Query / SWR |
| Realtime logs | Socket.IO-client ou WebSocket natif |
| Backend façade | FastAPI ou NestJS |
| Agent orchestration | Agno (gRPC/HTTP) ou LangChain |
| MCP Server | FastAPI + Redis (ou vector store) |
| Stockage/Mémoire | Postgres, Redis, pgvector |
| Déploiement | Google App Engine ou Cloud Run |
