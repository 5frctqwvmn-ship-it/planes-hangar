# Planes Hangar: progress archive

Nothing is thrown away. This branch keeps the before/after pictures from every build pass, so the story of how the game grew can be shown later. The game's own history lives in the `main` and `test` branches; every version of every file is still there.

## Run any old version of the game

Every milestone below is a git tag. To play the game exactly as it was:

```
git checkout <tag>
python3 -m http.server 8000
# open http://localhost:8000/index.html
```

You can also browse a tag on GitHub (Code > tags) to see the files as they were.

## Milestones

| Tag | Date | What changed |
|---|---|---|
| m01-start | 2026-10-23 | Earliest kept version |
| m02-maps-pass2 | 2026-10-30 | Themed scenery along every race line |
| m03-stability | 2026-10-31 | Course memory freed, graphics recovery, camera line of sight |
| m04-learn-levels | 2026-10-31 | Harder levels, new words, pictures, one try per question |
| m05-maps-declutter | 2026-10-31 | Fewer, better set pieces on every course |
| m06-angel | 2026-11-01 | Angel, the Blue Angels Super Hornet, with the formation win show |
| m07-airport | 2026-11-01 | Airport-style start screen |
| m08-ozzie | 2026-11-01 | Ozzie, the V-22 Osprey, plus the review fixes |
| m09-groundcrew | 2026-11-01 | Ground-crew vehicles as the audience |
| m10-liveries | 2026-11-01 | Navy, Arctic and desert ground-crew colours |

## Pictures

`images/<pass>/` holds the comparison sheets each build pass produced (before and after shots, strips of win shows, test frames). Folder names match the work: `maps` (course scenery passes), `stability` (camera fixes), `angel`, `osprey`, `groundcrew`, `livery`, `ships`, `airfield`, `learn`, `mathshow`, `review1`, `cabface`, `writeup` (the reviewer write-up and screenshot PDF).

## Old assets in the game itself

When a model is replaced, the old builder stays in the code behind a switch, so both can be filmed side by side:

- `?classic=ships` (or `?classic=all`): the warships, carriers and sailboats as they were before the ship upgrade.
