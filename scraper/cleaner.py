import os
import re

INPUT_FOLDER = "data/processed"

for filename in os.listdir(INPUT_FOLDER):

    if filename.endswith(".txt"):

        path = os.path.join(
            INPUT_FOLDER,
            filename
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            text = f.read()

        unwanted = [
            "Cookie Policy",
            "Manage Cookie Consent",
            "Accept",
            "Deny",
            "View preferences",
            "Skip to content"
        ]

        for item in unwanted:

            text = text.replace(
                item,
                ""
            )

        text = re.sub(
            r"\n{2,}",
            "\n",
            text
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(text)

print("Cleaning completed.")