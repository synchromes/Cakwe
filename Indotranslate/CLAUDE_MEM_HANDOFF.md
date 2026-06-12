# Milfs Plaza Indonesian Translation Memory

## Active Style Rules
- Natural Bahasa Indonesia, not literal.
- Do not censor, reduce, moralize, or soften explicit/harsh dialogue unless source tone requires nuance.
- Translate by meaning/context. Idioms use Indonesian intent, not word-for-word.
- Preserve Ren'Py syntax: labels, translate IDs, indentation, `{tags}`, `[placeholders]`, paths, variables.
- Keep source English/Russian as comments above translated lines when writing manual files.

## Relationship Glossary
- Mary/Marina/mother -> `Mama` / `Ma`; never `Ibu` in game dialogue.
- Direct casual call from MC -> `Ma` or `Mama` based on flow.
- Narration/ref to mother -> `Mama`.
- James/Father -> `Ayah`.
- Christie/sister -> kakak perempuan MC.
- MC -> Christie: `Kakak` / `Kak`.
- `your sister` -> `kakakmu`; `my sister` -> `kakakku`.
- Christie -> MC: `adik` / `adikku`.
- `You're my brother` -> `Kamu adikku`.
- `Brother's dick` -> `kontol adikku`.
- In hot scenes with Christie, still use `Kakak` / `Kak`.

## Sexual Glossary
- `boobs/breasts` normal context -> `payudara`.
- `boobs/tits` hot/sexual context -> `toket`.
- `pussy/vagina` hot context -> `memek`.
- `jerk off/stroke your cock` -> `coli`.
- `cum/come` sexual climax -> `keluar`.
- Use other Indonesian terms only if more natural in context.

## Completed Source Files
Progress basis: source files under `tl/eng/**/*.rpyc` = 370 total.
Completed: 49/370 = 13.24%/100%.

Completed staging files:
- `Indotranslate/core/BugReportSystem.rpy`
- `Indotranslate/core/GG_Room.rpy`
- `Indotranslate/core/TimeEvent.rpy`
- `Indotranslate/core/buttons_labels.rpy`
- `Indotranslate/core/cards_screen.rpy`
- `Indotranslate/core/descript_screen.rpy`
- `Indotranslate/core/main_interface.rpy`
- `Indotranslate/core/pc_interface.rpy`
- `Indotranslate/core/splashscreen.rpy`
- `Indotranslate/core/talk_with/check_surv.rpy`
- `Indotranslate/core/talk_with/milf_magic_label.rpy`
- `Indotranslate/core/talk_with/milf_sleep_label.rpy`
- `Indotranslate/core/talk_with/talk_with_clothes_store_woman.rpy`
- `Indotranslate/core/talk_with/talk_with_igor.rpy`
- `Indotranslate/core/talk_with/talk_with_jay_bob.rpy`
- `Indotranslate/core/talk_with/talk_with_kat_label.rpy`
- `Indotranslate/core/talk_with/talk_with_milf.rpy`
- `Indotranslate/core/talk_with/talk_with_night_girl.rpy`
- `Indotranslate/core/talk_with/talk_with_sister.rpy`

## Validation Routine
After every batch:
- Check all `.rpy`: even unescaped quotes, balanced `[]`, balanced `{}`.
- Search banned drift: `Ibu\b`, `tetek`, `Kocok kontol`, `kocok kontol`.
- Update `Indotranslate/_PROGRESS_ID.md` with completed/370 and percent.
- Report percent to user.

## MCP Note
claude-mem worker mode currently: semantic search transport error; `observation_add` requires server-beta, unavailable. Use `CLAUDE_MEM_HANDOFF.md` + `_PROGRESS_ID.md` as durable fallback; still try MCP search at major milestones.


## Latest Progress Update
- Completed root core batch: comic_frame_v2/v3/v4 + variables_at_start.
- Progress: 23/370 = 6.22%/100%.



## Latest Progress Update
- Bulk completed 14 core subfolder files.
- Progress: 37/370 = 10%/100%.



## Latest Progress Update
- Bulk completed 12 small events/top-level files.
- Progress: 49/370 = 13.24%/100%.

