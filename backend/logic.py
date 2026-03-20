from seed_data import TOPICS

def get_next_recommendation(topics):
    def checking_prerequisites(topic):
        topic_map = {t.id: t for t in topics}
        for prerequisite in topic.prerequisites:
            if topic_map[prerequisite].mastery_score < 100:
                return False
        return True
    for i in topics:
        if i.mastery_score < 100 and checking_prerequisites(i):
            return i
    return None

if __name__ == "__main__":
    print(get_next_recommendation(TOPICS))