# Script-Generator

This is a script generator.

If we have a file with bunch of Korean sentences, generator will preprocess it by removing unnecessary elements such as '!,?,*,(numbers), or repetitive words'. 

Then, it will change the sentences into diphones. diphone = ex) 마을 --> ㅏ-ㅇ, 망울 --> ㅇ-ㅇ (종성과 그다음 글자의 초성의 조합)

We can now have the frequencies of each diphones.

By implementing normalization equation, we can give scores for each sentences.

With the scores, we can select sentences that contain diphones with high frequencies.


This script generator can enhance the accuracy of TTS models.

* a file with bunch of Korean sentences and the results of each python file are in the release section.
