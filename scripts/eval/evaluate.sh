# generated from a612dbd60f49f41b2752d68b5c53b750eaf1f532
python evaluate.py \
    --prompt "Once upon a time," \
    --max_length 256 \
    --temperature 0.8 \
    --top_p 0.85 \
    --vocab_size 10000 \
    --context_len 256 \
    --d_model 512 \
    --num_layers 4 \
    --num_heads 16 \
    --d_ff 2048 \
    --attn_pdrop 0.1 \
    --resid_pdrop 0.1 \
    --checkpoint_path "./data/checkpoints/a612dbd60f49f41b2752d68b5c53b750eaf1f532_tiny_best_0.0003_128.pth" \
    --vocab_filepath "./data/TinyStoriesV2-GPT4-train_vocab.pkl" \
    --merges_filepath "./data/TinyStoriesV2-GPT4-train_merges.pkl"

# 'Once upon a time, there was a little boy named Tim. Tim had a toy car that he loved to play with.
# One day, Tim saw a girl named Sue playing with a toy car. Tim wanted to play with the car too,
# but he didn\'t know how to share.\nTim went to Sue and said, "Can I play with your car?" Sue
# looked at the car and thought for a moment. She said, "Okay, but you have to share it with me."
# Tim was very happy and played with the car.\nWhile they were playing, a big dog came and took the
# car in its mouth. Tim and Sue were sad. They thought the dog would take the car. But the dog ran
# away with the car. Tim and Sue chased the dog, but it was too fast.\nIn the end, Tim and Sue
# went home without the car. They were both very sad and had to leave their toy cars. The end.\n<|endoftext|>'