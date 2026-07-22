# Induction Heads in GPT-2 Small

Locating and **causally validating** the induction circuit in a small transformer — my first mechanistic-interpretability project, worked through the ARENA 1.2 material and written up from scratch.

**What this demonstrates:** that I can take a real model, form a mechanistic hypothesis, find the responsible components, and *prove* their role with causal interventions — not just read about interpretability.

## The result (what the write-up will claim)

1. **The phenomenon** — GPT-2 small is far better at predicting *repeated* random tokens than fresh ones (in-context copying), which points to a specific circuit.
2. **Localisation** — an induction-score heatmap over all (layer, head) pairs isolates a small number of **induction heads**.
3. **Mechanism** — the top induction head attends from the current token to *the token that followed its previous occurrence* (shown with attention-pattern visualisation).
4. **Causal proof** — ablating the induction heads spikes the loss on repeated sequences, confirming they *cause* the behaviour.
5. **The circuit** — the induction head is fed by an earlier **previous-token head** (head composition), completing the two-step circuit.

> Scope: this is a *skill-demonstration* write-up of a known result (Anthropic's induction-heads work), not novel research. The point is to show I can do the analysis. A follow-up would extend it to a novel circuit.

## Repo layout (fill as you go)

```
├── README.md              # this file
├── WRITEUP.md             # the narrative write-up (the actual deliverable)
├── requirements.txt
├── induction_heads.ipynb  # your working notebook (analysis + figures)
└── figures/               # exported plots for the write-up
```

## How it maps to my CV

Replaces the weak *"Interpretability (growing focus)"* line with a real entry:
> **Mechanistic Interpretability — Induction Circuits in GPT-2.** Located induction heads via induction-score analysis, visualised the attention pattern, and confirmed the circuit causally by ablation; traced the previous-token → induction-head composition. `transformer_lens`, public repo + write-up.

Status: 🚧 in progress.
