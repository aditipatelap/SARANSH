# use gensim version = 3.6.0
from gensim.summarization import summarize


def summaryMaker(text):
    summary = summarize(text, 0.3)
    # "ratio" parameter --> specify what fraction of sentences in the original text should be returned as output.
    #  default is 20% = 0.20
    # “word_count” parameter --> specify maximum amount of words we want in the summary.
    return summary

# ------ For Testing ------
# summary = summaryMaker(""" Modern Israel springs from both religious and political sources. The biblical promise of a land for the Jews and a return to the Temple in Jerusalem were enshrined in Judaism and sustained Jewish identity through an exile of 19 centuries following the failed revolts in Judaea against the Romans early in the Common Era. By the 1800s, fewer than 25,000 Jews still lived in their ancient homeland, and these were largely concentrated in Jerusalem, then a provincial backwater of the Ottoman Empire.
# In the 1880s, however, a rise in European anti-Semitism and revived Jewish national pride combined to inspire a new wave of emigration to Palestine in the form of agricultural colonies financed by the Rothschilds and other wealthy families. Political Zionism came a decade later, when the Austrian journalist Theodor Herzl began advocating a Jewish state as the political solution for both anti-Semitism (he had covered the sensational Dreyfus affair in France) and a Jewish secular identity. Herzl’s brief and dramatic bid for international support from the major powers at the First Zionist Congress (August 1897) failed, but, after his death in 1904, the surviving Zionist organization under the leadership of Chaim Weizmann undertook a major effort to increase the Jewish population in Palestine while continuing to search for political assistance.
# These efforts could only be on a small scale while the Ottoman Turks ruled what the Europeans called Palestine (from Palaestina, “Land of the Philistines,” the Latin name given Judaea by the Romans). But in 1917, during World War I, the Zionists persuaded the British government to issue the Balfour Declaration, a document that committed Britain to facilitate the establishment of a “Jewish homeland” in Palestine. Amid considerable controversy over conflicting wartime promises to the Arabs and French, Britain succeeded in gaining the endorsement of the declaration by the new League of Nations, which placed Palestine under British mandate. This achievement reflected a heady mixture of religious and imperial motivations that Britain would find difficult to reconcile in the troubled years ahead. """)
#
# print(summary)
