import streamlit as st

def calculate_like(importance_same_race, d_age, samerace, attractive_partner, sincere_partner, intelligence_partner,
                   funny_partner, ambition_partner, shared_interests_partner, allocated_points, guess_prob_liked, intelligence_important, funny_important, sincere_important):
    if funny_partner <= 4.50:
        if funny_partner <= 1.50:
            return 2.05
        else:
            if attractive_partner <= 3.50:
                if intelligence_partner <= 7.50:
                    if guess_prob_liked <= 2.50:
                        return 1.88
                    else:
                        return 3.06
                else:
                    return 4.75
            else:
                if guess_prob_liked <= 3.50:
                    if ambition_partner <= 8.50:
                        if funny_important <= 13.50:
                            return 4.19
                        else:
                            return 3.24
                    else:
                        return 5.50
                else:
                    if ambition_partner <= 8.50:
                        if funny_important <= 12.50:
                            return 6.20
                        else:
                            if sincere_partner <= 4.50:
                                return 3.60
                            else:
                                return 5.38
                    else:
                        return 3.50
    else:
        if shared_interests_partner <= 6.50:
            if attractive_partner <= 5.50:
                if ambition_partner <= 4.50:
                    if shared_interests_partner <= 3.50:
                        return 2.00
                    else:
                        if guess_prob_liked <= 2.50:
                            if sincere_important <= 12.50:
                                return 5.67
                            else:
                                if sincere_important <= 20.50:
                                    return 3.33
                                else:
                                    return 5.25
                        else:
                            if intelligence_partner <= 8.50:
                                return 5.45
                            else:
                                return 7.14
                else:
                    if guess_prob_liked <= 2.50:
                        return 5.67
                    else:
                        if intelligence_partner <= 8.50:
                            return 5.45
                        else:
                            return 7.14
            else:
                if shared_interests_partner <= 4.50:
                    if importance_same_race <= 8.50:
                        if funny_partner <= 6.50:
                            if sincere_partner <= 7.50:
                                return 5.34
                            else:
                                if attractive_partner <= 8.50:
                                    return 6.12
                                else:
                                    return 8.00
                        else:
                            return 6.84
                    else:
                        if samerace <= 0.50:
                            return 3.25
                        else:
                            return 5.50
                else:
                    if attractive_partner <= 7.50:
                        if intelligence_partner <= 9.50:
                            if guess_prob_liked <= 6.50:
                                return 6.24
                            else:
                                return 6.83
                        else:
                            return 7.23
                    else:
                        return 7.20
        else:
            if attractive_partner <= 7.50:
                if guess_prob_liked <= 4.50:
                    if attractive_partner <= 5.50:
                        return 4.56
                    else:
                        return 6.71
                else:
                    if guess_prob_liked <= 7.50:
                        return 7.07
                    else:
                        if intelligence_important <= 19.00:
                            return 6.88
                        else:
                            return 7.97
            else:
                if shared_interests_partner <= 7.50:
                    if funny_partner <= 8.50:
                        return 7.28
                    else:
                        return 8.27
                else:
                    if shared_interests_partner <= 9.50:
                        return 8.64
                    else:
                        return 9.61

def main():
    st.title("Partner Liking Calculator")

    st.write("Please answer the following questions:")

    importance_same_race = st.slider("How important is it to you that your partner is of the same race? (1-10)", 1, 10)
    d_age = st.number_input("What is the age difference between you and your partner?", min_value=0.0, step=0.1)

    samerace = st.radio("Are you and your partner of the same race?", ('Yes', 'No'))

    attractive_partner = st.slider("On a scale of 1-10, how attractive do you find your partner?", 1, 10)
    sincere_partner = st.slider("On a scale of 1-10, how sincere do you find your partner?", 1, 10)
    intelligence_partner = st.slider("On a scale of 1-10, how intelligent do you find your partner?", 1, 10)
    funny_partner = st.slider("On a scale of 1-10, how funny do you find your partner?", 1, 10)
    ambition_partner = st.slider("On a scale of 1-10, how ambitious do you find your partner?", 1, 10)
    shared_interests_partner = st.slider("On a scale of 1-10, how many shared interests do you have with your partner?", 1, 10)

    allocated_points = {}
    remaining_points = 100
    characteristics = ['Attractiveness', 'Sincerity', 'Intelligence', 'Funniness', 'Ambition', 'Shared Interests']
    for characteristic in characteristics:
        points = st.slider(f"Allocate points for {characteristic}:", 0, remaining_points)
        allocated_points[characteristic] = points
        remaining_points -= points

    guess_prob_liked = st.slider("On a scale of 1-10, how much do you think your partner likes you?", 1, 10)

    if st.button("Calculate"):
        inputs = (importance_same_race, d_age, 1 if samerace == 'Yes' else 0, attractive_partner, sincere_partner,
                  intelligence_partner, funny_partner, ambition_partner, shared_interests_partner,
                  allocated_points, guess_prob_liked)
        like_value = calculate_like(*inputs)
        st.write(f"Based on your inputs, your liking score for your partner is: {like_value}")

if __name__ == "__main__":
    main()
