def format_profile(profile):
    additional_skills = [s["skill"] for s in profile.get("additionalSkill", []) if isinstance(s, dict) and "skill" in s]
    highlighted_skills = [s for s in profile.get("highlightedSkills", []) if isinstance(s, str)]

    return f"""
    Profile:
    Name: {profile.get('firstName')} {profile.get('lastName')}
    Area of Expertise: {profile.get('areaOfExpertise')}
    Summary: {profile.get('carrierSummary')}

    Experience: {profile.get('experience', [])}
    Education: {profile.get('education', [])}
    Additional Skills: {', '.join(additional_skills)}
    Highlighted Skills: {', '.join(highlighted_skills)}
    """
