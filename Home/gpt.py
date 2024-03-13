import openai


def get_response(character, theme):
    form_data = "Can you, please, create some content on the theme: '{0}', " \
                "specifically tailored for a character named: '{1}', depending on the answers to such questions:" \
                "What forms of art do you enjoy the most?: {2}, " \
                "Do you prefer traditional or contemporary art?: {3}, " \
                "Which artists or art movements inspire you?: {4}, " \
                "What emotions or messages do you aim to convey through your art?: {5}, " \
                "Are there any specific themes or subjects that frequently appear in your artwork?: {6}, " \
                "Do you prefer creating art independently or collaborating with others?: {7}, " \
                "What role does art play in your life?: {8}, " \
                "How do you handle criticism or feedback about your artwork?: {9}, " \
                "Do you have any long-term goals or aspirations for your artistic journey?: {10}, " \
                "How do you approach the creative process?: {11}, " \
                "How important is technical skill versus personal expression in your artwork?: {12}, " \
                "How do you feel about experimenting with new techniques or styles?: {13}, " \
                "Is there a particular audience or demographic you intend to connect with through your art?: {14}, " \
                "Are there any specific cultural or historical influences that shape your artistic style?: {15}" \
                "".format(theme, character.name, character.art_forms, character.art_preference,
                          character.art_inspiration, character.art_emotions, character.art_themes,
                          character.art_creation, character.art_role, character.art_feedback,
                          character.art_goals, character.creative_process, character.technical_skill,
                          character.art_experimentation, character.target_audience,
                          character.cultural_influences)

    # final_data = gpt_request(form_data=form_data)
    return form_data


def gpt_request(form_data):
    openai.api_key = "INSERT THE API TOKEN HERE"
    completion = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=f"{form_data}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return completion.choices[0].text
