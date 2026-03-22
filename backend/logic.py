from seed_data import TOPICS

def get_next_recommendation(topics):
    def checking_prerequisites(topic):
        topic_map = {t.id: t for t in topics}
        # Split "id1,id2" into ["id1", "id2"]
        prereqs = [p.strip() for p in topic.prerequisites_raw.split(",") if p.strip()]
        for prerequisite in prereqs:
            if topic_map[prerequisite].mastery_score < 100:
                return False
        return True
    for i in topics:
        if i.mastery_score < 100 and checking_prerequisites(i):
            return i
    return None

if __name__ == "__main__":
    print(get_next_recommendation(TOPICS))