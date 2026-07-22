"""
Induction Heads in GPT-2 Small — working script.
Run:  .venv/bin/python induction_heads.py
Fill each STEP as you go (mirrors the ARENA 1.2 exercises). Paste your code + result to me after each.
"""
import torch
import matplotlib
matplotlib.use("Agg")            # save figures to files, no GUI needed
import matplotlib.pyplot as plt
from pathlib import Path
from transformer_lens import HookedTransformer

Path("figures").mkdir(exist_ok=True)
device = "mps" if torch.backends.mps.is_available() else "cpu"
model = HookedTransformer.from_pretrained("gpt2-small", device=device)
print(f"Loaded gpt2-small on {device}")

# =========================================================================
# STEP 1 — The phenomenon: in-context copying on repeated random tokens
# =========================================================================
# Goal: show GPT-2 predicts the SECOND copy of a random sequence far better than
# the first. Per-position log-prob of the correct next token should JUMP UP right
# after the repeat boundary. That jump is the induction heads doing their thing.
#
# TODO (write this yourself — it's ~8 lines):
#   1) Build `tokens`: a BOS token, then the SAME random sequence TWICE.
#        - random ids: torch.randint over model.cfg.d_vocab, length seq_len (try 50)
#        - assemble with torch.cat -> shape [1, 1 + 2*seq_len]
#   2) Run the model -> logits; convert to log-probs; pull out the log-prob of the
#      ACTUAL next token at each position (hint: gather, or advanced indexing).
#   3) plt.plot the per-position log-prob, draw a vertical line at x = seq_len,
#      and plt.savefig("figures/step1_phenomenon.png").
#
# Then READ the plot: where does it jump? Roughly how big is the improvement?

raise NotImplementedError("Implement STEP 1, run this file, then open figures/step1_phenomenon.png")

# =========================================================================
# STEP 2 — Localise induction heads (induction-score heatmap over all heads)
# STEP 3 — Attention pattern of the top head (circuitsvis)
# STEP 4 — Causal ablation (ablate the heads -> loss on repeats spikes)
# STEP 5 — The circuit: previous-token head -> induction head (composition)
# =========================================================================
