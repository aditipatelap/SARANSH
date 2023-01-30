from transformers import AutoTokenizer, AutoModelWithLMHead
import SummaryToVoice

tokenizer = AutoTokenizer.from_pretrained('t5-base')
model = AutoModelWithLMHead.from_pretrained('t5-base', return_dict=True)

# text = """The Pythonidae, commonly known as pythons, are a family of nonvenomous snakes found in Africa, Asia, and Australia. Among its members are some of the largest snakes in the world. Ten genera and 42 species are currently recognized. Being naturally non-venomous, pythons must constrict their prey to suffocate it prior to consumption. Pythons will typically strike at and bite their prey of choice to gain hold of it; they then must use physical strength to constrict their prey, by coiling their muscular bodies around the animal, effectively suffocating it before swallowing whole. This is in stark contrast to venomous snakes such as the rattlesnake, for example, which delivers a swift, venomous bite but releases, waiting as the prey succumbs to envenomation before being consumed. Collectively, the pythons are well-documented and -studied as constrictors, much like other non-venomous snakes, including the boas and even kingsnakes of the New World.[2]"""


def summrizer(text, max_length=150, min_length=80):
    print("Start prcossesing to summarize text.")
    SummaryToVoice.voice("Start prcossesing to summarize text.")
    inputs = tokenizer.encode("summarize: " + text,
                              return_tensors='pt',
                              max_length=512,
                              truncation=True)

    summary_ids = model.generate(
        inputs, max_length=max_length, min_length=min_length, length_penalty=5., num_beams=2)

    summary = tokenizer.decode(summary_ids[0])

    return summary


# print(summrizer(text))