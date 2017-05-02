#!/usr/bin/env bash
rm -f INF5860_Oblig2.zip
zip -r INF5860_Oblig2.zip . -x "*.git*" "*datasets*" "*.ipynb_checkpoints*" "*README.md" "*collectSubmission.sh" "*requirements.txt" ".env/*" "*.pyc"
