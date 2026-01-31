# Phase 23 Development Diary

## Test Scripts and Video Recordings

## What this is

Mr Davies said I should record myself actually testing the app to prove it works, not just have the written test log. Fair enough. So I went back and wrote proper test scripts for the 7 main features and recorded screen captures of each one.

This is the final phase diary entry. Earlier phase entries are in Git history because I kept this as a working document.

## The videos

1. Model training (Phase 3 terminal) -- just the MLP training running in the terminal
2. Image upload predictions (Phase 7) -- uploading digit images and getting predictions
3. CNN comparison training (Phase 11) -- training all three architectures back to back
4. Database history (Phase 13) -- showing runs saving to SQLite and appearing in the table
5. Charts dashboard (Phase 15-16) -- the Plotly accuracy and training time charts
6. Error handling and drawing (Phase 20) -- input validation, the drawing canvas, edge cases
7. Full end-to-end system demo -- everything working together from scratch

## How long

About 4 hours across two evenings (5th-6th Feb). Writing the scripts was quick but had to redo a couple recordings when things went wrong. The CNN training one took ages because it actually trains 3 models in the recording. I named the folders by the date of the phase they're testing, not when I actually recorded them -- probably shouldn't have done that but I'd already committed them before I thought about it.

## Problems I hit

- First recording of the upload prediction test had a rubbish example image, so the confidence looked low and confusing. Re-recorded it with a clearer digit.
- One run had me clicking around tabs too fast and I skipped a step from the script, so that take was useless and I had to start again.
- The full end-to-end recording was the most annoying because if one bit goes wrong near the end, you lose the whole take.
- Audio wasn't needed, but I still had to keep notes nearby so I didn't forget what each clip was meant to prove.

## Testing I did for this phase

- Ran the app and checked all three tabs before recording.
- Did one dry run for each script without recording, just to make sure no obvious errors popped up.
- Re-ran model prediction checks after recording to confirm outputs were still sensible.
- Opened the generated folders and checked each one had both `test_script.md` and `recording.webm`.

## Why this phase still matters

No new feature code here, but this phase is still part of the build story because it proves the existing features actually work in practice. It also made me notice small UX bits I'd ignore during coding.

## Reflection

This phase felt less technical and more about evidence quality. Bit boring at times, but useful. The main thing I learned is that "it works on my machine" isn't enough unless I can show it clearly. Recording proper demos forced me to be more honest about rough edges.

If I did this again, I'd start recording evidence earlier in the project instead of leaving most of it to the end.

## What I learned

Recording yourself doing something is way harder than just doing it. You notice all the little UI glitches you normally ignore. But it's decent evidence that everything actually works and I'm not just saying it does in the test log.

## Time spent

- Script prep and tidy-up: ~1 hour
- Recording takes (including re-dos): ~2 hours
- File checks and organising folders: ~1 hour
