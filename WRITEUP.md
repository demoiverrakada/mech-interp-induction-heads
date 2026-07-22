# Finding Induction Heads in GPT-2 Small

*(Fill each section as you complete the corresponding step. Keep it short and figure-driven — a good interp write-up is mostly plots with tight captions.)*

## TL;DR
<!-- 2–3 sentences: what you set out to find and what you found. Write this LAST. -->

## 1. The phenomenon: in-context copying
<!-- Show the loss on a sequence of random tokens repeated twice. The model is much better on the
     second copy. Plot per-position loss; point to the drop after the repeat boundary. -->

## 2. Locating the induction heads
<!-- Define induction score (avg attention to the token that followed the previous occurrence,
     offset -seq_len+1 on the diagonal). Compute it for every (layer, head). Heatmap. Name the top heads. -->

## 3. What the top head is doing
<!-- circuitsvis attention pattern for the top induction head on a repeated sequence.
     Show it attends current-token -> token-after-previous-occurrence. -->

## 4. Causal validation by ablation
<!-- Mean-ablate (or zero-ablate) the induction heads and re-measure loss on repeated sequences.
     Loss should spike. This proves the heads *cause* the copying, not just correlate. -->

## 5. The circuit: previous-token head → induction head
<!-- Identify the layer-0 previous-token head feeding the induction head (K-composition).
     Optionally: ablate the prev-token head and show the induction head breaks. -->

## Method / setup
<!-- Model (gpt2-small via transformer_lens), how sequences were generated, ablation method, hardware. -->

## Limitations & next steps
<!-- Known result (not novel); single model; ablation is coarse. Next: a novel circuit / larger model / SAEs. -->
