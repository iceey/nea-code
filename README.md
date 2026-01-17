# Phase 21: Empty State Messages + UI Polish

## What Changed

- Added empty state messages to all History tab charts
- Expanded predict function to return 4 values (added results table + consensus)
- Fixed consensus logic firing with only one model
- Added a little intro message to Train and Predict tabs for new users

This grew from a 30-minute task to about 2.5 hours because testing the empty states kept turning up more stuff to fix. Kind of annoying but that's what this phase was for.

## Empty State Charts

Instead of returning `None` (blank chart), empty-data paths now return a Plotly figure with a centred annotation:

```python
fig.add_annotation(
    text="No training history\n\nTrain a model to see charts!",
    xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False
)
```

Used `xref="paper"` coordinates so the text sits at (0.5, 0.5) regardless of axis ranges. Grey text for empty states, red for errors. Hidden axes since they'd just show 0-1 with no data.

## Predict Function Changes

**Added results table + consensus output**: Expanded the predict function from returning 3 values to 4 (original image, preprocessed image, results dataframe, consensus text). This meant updating every if/else branch to return the right number of values with an empty DataFrame for error paths. Gradio throws a `ValueError` if the count doesn't match the outputs list, so I had to be thorough.

**Consensus guard**: One of the consensus checks was running even with a single model, which would show "All models agree!" -- technically true but meaningless. Added `len(clean_preds) >= 2` so it only shows when there are multiple models to compare.

## What You See on First Launch

Also noticed the Train and Predict tabs had the same blank-screen problem on first launch. Train tab now shows a guide with the three architectures and rough training times. Predict tabs show "Waiting for input..." pointing to the upload/draw area. Prevents the "what am I supposed to do?" moment.

## Testing

Wiped the database and tested fresh launch - every tab has clear guidance. Trained a couple of models, verified empty states disappear once there's real data. Checked predict function with various error conditions to confirm the 4-tuple fix. Tested with just one trained model for the consensus check.

I'd been skipping this stuff while I was building features but it actually makes a massive difference to how finished it feels.

## Decisions

### Centring the Message When There's No Data

```python
xref="paper", yref="paper", x=0.5, y=0.5
```

Using `"paper"` coordinates means 0.5 is always the middle of the chart, no matter what the axes say. For an empty chart with no data, the axes don't mean anything anyway. If I used normal x/y coordinates the text would end up in a weird position.

### Same Chart Height Whether Empty or Not

Both the empty-state charts and the ones with actual data use `height=400`. If they were different heights, the page would jump around when switching between empty and filled charts which would look janky.

### All DataFrame Columns as Strings

Even though confidence is a number, I format it with a `%` sign (like `"93.4%"`). So I set all the column types to `"str"` to stop Gradio trying to do number sorting on something that has a percentage sign in it.

### Chaining Updates With `.then()`

The predict button uses `.then()` so the chart refreshes after the prediction finishes. If they ran at the same time the chart might not have the latest data because the prediction hasn't saved to the database yet. `.then()` makes them run one after the other.

## How to Run

```bash
python init_db.py
python app_ui.py
```

On first launch, every tab now shows guidance instead of blank space.

## Differences from Phase 20

| Aspect | Phase 20 | Phase 21 |
|--------|----------|----------|
| **Empty states** | Blank charts / None | Annotated Plotly figures with messages |
| **Predict output** | 3 values (images + text) | 4 values (images + DataFrame + consensus) |
| **First launch** | Blank tabs | Guidance text on all tabs |
| **Consensus** | Always shown | Only with 2+ models |
| **app_ui.py** | 786 lines | 935 lines (+149) |
