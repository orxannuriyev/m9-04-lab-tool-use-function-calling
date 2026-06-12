![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Lab | Give the Model Hands

## Overview

So far the model has only produced words. Today you give it the ability to **act** — by letting it call tools. You'll define two tools, hand them to the model with **native Gemini function calling**, and watch the model→tool→model loop play out: the model asks for a tool, *your code* runs it, the result goes back, and the model finishes the job. You'll see, directly, that the model only ever **asks** — your code does the doing.

The task it can't solve alone needs **two tools used together**, so you'll see the loop go round more than once.

## Learning Goals

- Describe tools to a model with a schema (name, description, parameters)
- Run the tool-use loop: receive a tool call, validate it, execute it, return the result
- Chain two tool calls to answer a question neither tool could answer alone

## Setup

Fork, clone, branch. Reuse your Gemini key.

```bash
pip install -r requirements.txt
export GOOGLE_API_KEY="your-free-gemini-key"
```

You're given `orders.json`, a tiny order database. Work in `tool_use.ipynb` or `.py`.

## Your Task

**Give the model two tools and let it answer a question that needs both.**

1. Define **two tools** and describe each with a clear schema:
   - `lookup_order(order_id)` — returns the order's item, price, purchase date, and warranty length from `orders.json`.
   - `calculate(expression)` — evaluates a simple arithmetic expression and returns the number. (The model is unreliable at exact math — this is why it needs the tool.)
2. Wire up the **tool-use loop** with native Gemini function calling: when the model emits a tool call, your code **validates the arguments**, runs the real function, and returns the result to the model. Loop until the model produces a final answer.
3. Ask a question that requires **both tools in sequence**, for example:
   > *"For order A1001, what would the total be if I bought three of them?"*

   The model should call `lookup_order` to get the price, then `calculate` to multiply by three, then answer.
4. Also send one question that needs **no tool** (e.g. `"What can you help me with?"`) and confirm the model just answers directly without calling anything.

Your deliverable should show the tool calls the model made (which tool, what arguments) and the final answers — so the loop is visible.

### Optional stretch

Make the model produce a **bad argument** on purpose (ask about a non-existent order like `A9999`). Have your `lookup_order` return a clear "order not found" result and confirm the model handles it gracefully instead of crashing.

## Submission

Commit your code and a short transcript (or notebook output) showing the tool calls and answers for both questions. Open a PR and paste the link.

## Quality Bar

- Each tool has a clear schema the model can act on
- Your code **validates and runs** the tools; the model only requests them
- The two-tool question visibly triggers both calls in sequence
- The no-tool question is answered directly, with no tool call
- No API key is committed
