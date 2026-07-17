from rapidfuzz import fuzz


class PriceMatcher:

    def barkod(self, barkod, liste):

        if barkod in liste:
            return liste[barkod]

        return None

    def isim(self, isim, liste):

        en_yuksek = 0
        sonuc = None

        for urun in liste:

            puan = fuzz.ratio(
                isim.upper(),
                urun.upper()
            )

            if puan > en_yuksek:
                en_yuksek = puan
                sonuc = urun

        if en_yuksek >= 92:
            return sonuc

        return None