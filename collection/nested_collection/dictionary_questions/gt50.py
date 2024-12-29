students_score={"Anu":60,"mahi":50,"arjun":75,"danu":40,"hari":95}

filtered_scores={k:v for k,v in students_score.items() if v>50}

print(filtered_scores)


