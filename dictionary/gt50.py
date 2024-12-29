students_score={"Ammu":60,"malu":50,"anu":75,"damu":40,"hari":95}

filtered_scores={k:v for k,v in students_score.items() if v>50}

print(filtered_scores)

