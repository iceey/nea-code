# Phase 21 Development Diary

## What Started As

Was supposed to be quick. Just add empty state messages to the History tab charts so new users don't see blank white rectangles. Instead of returning None when there's no data, return a Plotly figure with a centred annotation saying "No training history yet - train a model to see charts."

Used `xref="paper"` coordinates so the text sits at (0.5, 0.5) regardless of axis ranges. Grey text for empty states, red for actual errors. Hid the axes since they'd just show 0-1 with no data. With `showarrow=False` and the axes hidden, it's just the message on a blank background, which is what I wanted.

## What It Turned Into

Testing the empty states turned into a whole thing. I wanted to add a proper results table and consensus message to the prediction output, which meant changing the predict function from returning 3 values to 4 (original image, preprocessed image, dataframe, consensus text). Had to go through every if/else branch and update them all to return 4 things, using an empty DataFrame when there's an error. Gradio threw ValueErrors whenever a return path had the wrong count, so I had to be careful.

While I was at it, noticed one of the consensus checks was running even when only one model was available - it would show "All models agree!" which is technically true but meaningless. Added a `len(clean_preds) >= 2` guard so the consensus message only appears when there are actually multiple models to compare.

Then I looked at the Train and Predict tabs and realised they had the same blank-screen problem on first launch. The Train tab now shows a little guide with the three architectures and rough training times so new users know what to expect. The Predict tabs show "Waiting for input..." in the results table with a message pointing to the upload/draw area. It's not fancy but it prevents that "what am I supposed to do?" moment.

## Testing

Wiped the database and tested fresh launch - every tab now has clear guidance instead of blank space. Trained a couple of models and verified the empty states disappear properly once there's real data. Checked the predict function with various error conditions to confirm the 4-tuple fix works. Also tested with just one trained model to make sure the consensus message doesn't show.

The return value changes cascaded through more of the code than I expected. Wasn't planning on restructuring the predict function but once I started adding the results table it made sense to do it properly.

## Reflection

What I thought would take 30 minutes ended up being about 2.5 hours because of all the extra fixes. Annoying but thats kind of the point of a polish phase I suppose. I'd been ignoring this stuff while building features but it's really what stops the app looking half-done. The app feels way more finished now - no more blank screens when you first open it. Didn't realise how much all those small details would add up.
