import json
import os


class ColumnMapper:

    def __init__(self):

        self.profiles_folder = "profiles"

        if not os.path.exists(self.profiles_folder):
            os.makedirs(self.profiles_folder)

    def basliklari_oku(self, worksheet):

        basliklar = []

        for hucre in worksheet[1]:

            if hucre.value is None:
                continue

            basliklar.append(str(hucre.value).strip())

        return basliklar

    def profil_kaydet(self, firma, mapping):

        dosya = os.path.join(
            self.profiles_folder,
            firma.lower() + ".json"
        )

        with open(dosya, "w", encoding="utf-8") as f:

            json.dump(
                mapping,
                f,
                ensure_ascii=False,
                indent=4
            )

    def profil_yukle(self, firma):

        dosya = os.path.join(
            self.profiles_folder,
            firma.lower() + ".json"
        )

        if not os.path.exists(dosya):
            return None

        with open(dosya, "r", encoding="utf-8") as f:
            return json.load(f)