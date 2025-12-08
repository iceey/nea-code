# Phase 14 Development Diary

## What Happened

Phase 13 had a simple single-model prediction - you upload an image, it predicts with whatever model was loaded. But the plan was always to compare all three architectures automatically and show results side by side. So this phase was rewriting the predict tab from scratch to do that.

Bit more work than expected honestly. The old predict function was straightforward (one model, one result), and the new version has to query the database, find the best model per architecture, load each one, run predictions, and show everything together with a consensus check.

## The Actual Comparison Feature

Wrote a `get_best_models()` function that queries the database for the highest-accuracy model per architecture (Phase 12's database schema made this pretty easy - just ORDER BY val_accuracy DESC LIMIT 1 for each architecture). Then `predict_with_comparison()` loads each best model, runs the prediction, and shows all results together with a consensus check at the end.

The consensus bit is satisfyingly simple - just check if `len(set(predictions)) == 1`. If all models agree, they're probably right. If they disagree, that's interesting information too.

The `set()` thing works because sets can't have duplicates - so `set([3, 3, 3])` just becomes `{3}` and has length 1, meaning all models agreed. If one disagrees it'd be something like `{3, 7}` with length 2. Didn't know you could use sets like that, found it on Stack Overflow.

Also started using list comprehensions here - instead of doing a for loop with `.append()` you can write `[row[0] for row in data]` and it builds the list in one go. Reads as "grab the first element from each row". We never did these in class but they seem to be all over the place in Python. Took a bit to get used to reading them but they're way shorter than the loop version.

## Small CNN Corruption

Of course it couldn't just work first time. MLP and Deeper CNN loaded fine, but the Small CNN threw

```
File not found: filepath=artifacts/model_small_cnn_run3.keras
```

which was confusing because `os.path.exists()` returned True. The file was there, 4.2MB, looked normal. Keras just couldn't read it - I think it was saved with a different TensorFlow version and the format is slightly incompatible. Spent about 20 minutes trying different things before giving up and just retraining a new Small CNN. New model saved and loaded perfectly.

So now I know: just because a file exists doesn't mean Keras can open it. Wrapping `load_model()` in try/except from now on.

## Testing

Uploaded a test image and got:

```
MLP: Predicted 3 (Conf: 85.2%)
Small CNN: Predicted 3 (Conf: 74.3%)
Deeper CNN: Predicted 2 (Conf: 58.0%)

Disagreement: Models predict different digits
```

Which is actually a good result because it shows the feature working properly - the models genuinely disagree sometimes and now you can see that. App launches fine, all tabs work.

## Reflection

The comparison approach turned out way better than single-model prediction - you can see all three predictions at once and the consensus check is actually useful. The corrupted model file was unexpected but it's good to know that can happen.

Hour and a half maybe.
