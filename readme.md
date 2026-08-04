# Trendly AI Customer Support Agent

An AI-powered customer support assistant built using **FastAPI**, **LangGraph**, **LangChain**, **NVIDIA AI Endpoints**, and **FAISS**. The assistant answers customer queries related to orders, shipping, returns, refunds, and exchanges by combining tool calling with Retrieval-Augmented Generation (RAG).

---

# Features

- AI-powered customer support chatbot
- Order tracking using Order ID
- Shipping policy lookup
- Return eligibility checking
- Return creation
- Refund policy assistance
- Exchange policy assistance
- Human escalation support
- Retrieval-Augmented Generation (RAG) using FAISS
- Tool calling using LangGraph
- REST API using FastAPI
- Automatic API documentation with Swagger

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| FastAPI | REST API |
| LangGraph | AI Agent Workflow |
| LangChain | LLM Orchestration |
| NVIDIA AI Endpoints | Chat Model & Embeddings |
| FAISS | Vector Database |
| Pydantic | Data Validation |
| Markdown | Knowledge Base |

---

# Project Structure

```
trendly/
│
├── app/
│   ├── api/
│   │   └── chat.py
│   │
│   ├── prompts/
│   │   └── system_prompt.py
│   │
│   └── policy/
│       └── trendly_policy.md
│
├── graph/
│   ├── graph.py
│   ├── state.py
│   └── langchain_tools.py
│
├── services/
│   ├── llm.py
│   ├── order_service.py
│   └── vector_store.py
│
├── tools/
│   ├── order_lookup.py
│   ├── policy_search.py
│   ├── eligibility_check.py
│   ├── return_action.py
│   └── escalate.py
│
├── data/
│   └── orders.json
│
├── models.py
├── main.py
├── requirements.txt
└── README.md
```

---

# Architecture

```
                User

                  │

                  ▼

             FastAPI API

                  │

                  ▼

            LangGraph Agent

        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
      NVIDIA LLM        ToolNode
                            │
        ┌───────────────────┼────────────────────┐
        │                   │                    │
        ▼                   ▼                    ▼
 Order Lookup       Policy Search       Return Eligibility
                                            │
                                            ▼
                                     Return Creation
                                            │
                                            ▼
                                     Human Escalation
```

---

# AI Workflow

```
Customer

↓

FastAPI

↓

LangGraph

↓

LLM

↓

Tool Selection

↓

Tool Execution

↓

LLM

↓

Final Response
```

---

# Available Tools

## Order Lookup

Retrieves:

- Order Status
- Tracking Number
- Carrier
- Expected Delivery
- Ordered Items
- Payment Method

---

## Policy Search

Uses FAISS + NVIDIA Embeddings to search the Trendly policy document for:

- Shipping
- Returns
- Refunds
- Exchanges
- Delays
- Lost Parcels

---

## Eligibility Check

Checks whether an order is eligible for return based on:

- Delivery status
- 30-day return window
- Final Sale restrictions
- Non-returnable categories
- Refund status

---

## Return Action

Creates a return request for eligible orders.

---

## Escalation

Escalates conversations requiring human assistance, such as:

- Lost parcels
- Unsupported policy requests
- Requests requiring manual verification

---

# API Endpoint

## POST /chat

### Request

```json
{
    "session_id": "session-1",
    "message": "Track my order TR-4521"
}
```

### Response

```json
{
    "reply": "Your order TR-4521 is currently in transit...",
    "escalated": false
}
```

---

# Example Queries

Track an order

```
Track order TR-4521
```

Return eligibility

```
Can I return order TR-4530?
```

Shipping policy

```
What is your shipping policy?
```

Refund policy

```
How long do refunds take?
```

Exchange policy

```
Can I exchange my shirt?
```

Human support

```
I want to talk to a human agent.
```

---

# RAG Pipeline

```
Policy Markdown

↓

Markdown Loader

↓

Text Splitter

↓

NVIDIA Embeddings

↓

FAISS

↓

Retriever

↓

LLM
```

---

# LangGraph Workflow

```
START

↓

Assistant

↓

Tool Needed?

├── No ─────────► END

└── Yes

↓

ToolNode

↓

Assistant

↓

END
```

---

# Running the Project

## Clone

```bash
git clone <repository-url>
cd trendly
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
MODEL_NAME=<your_nvidia_chat_model>

NVIDIA_API_KEY=<your_api_key>

NVIDIA_EMBEDDINGS_API_KEY=<your_embedding_key>
```

---

## Run

```bash
uvicorn main:app --reload
```

---

## Swagger

```
http://127.0.0.1:8000/docs
```

---

# Sample Test Cases

| Query | Expected Behaviour |
|--------|--------------------|
| Track TR-4521 | Order Lookup |
| Return TR-4530 | Eligible |
| Return TR-4523 | Outside Return Window |
| Return TR-4527 | Jewellery Not Returnable |
| Return TR-4528 | Exchange Only |
| Track TR-4526 | Escalate Human |
| Track TR-4525 | Delayed Order |
| Track TR-4524 | Partial Shipment |
| Return TR-4529 | Already Cancelled |

---

# Future Improvements

- Conversation Memory
- Persistent Chat History
- Authentication
- Database Integration
- Admin Dashboard
- Multi-language Support
- Streaming Responses
- WebSocket Support

---

# Author

**Vishnu Vardhan Nayak**

AI & Software Developer

Built as part of the **Trendly Founding AI Engineer Assignment**.