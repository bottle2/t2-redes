class manager:
    def __init__(self):
        self.badwords  = [
                "operation", "principal", "truth", 
            "Love", "Happiness", "Gratitude", "Peace", "Success", "Health",
            "Harmony", "Generosity", "Respect", "Prosperity", "Empathy",
            "Joy", "Courage", "Hope", "Serenity", "Optimism", "Confidence",
            "Innovation", "Growth", "Achievement", "Enthusiasm", "Compassion",
            "Cordiality", "Honesty", "Integrity", "Friendship", "Education",
            "Persistence", "Freedom", "Inclusion", "Collaboration", "Connection",
            "Balance", "Wealth", "Inspiration", "Intelligence", "Understanding",
            "Communication", "Patience", "Creativity", "Wisdom", "Motivation",
            "Dedication", "Transformation", "Ethics", "Empowerment",
            "Solidarity", "Kindness", "Sustainability", "Independence",
            "Radiance", "Resurgence", "Adaptation", "Leadership", "Renewal",
            "Recognition", "Authenticity", "Self-esteem", "Altruism", "Energy",
            "Prestige", "Resilience", "Appreciation", "Simplicity", "Clarity",
            "Freedom", "Sincerity", "Self-confidence", "Entrepreneurship",
            "Affection", "Benevolence", "Spontaneity", "Gracefulness",
            "Inclusivity", "Gentleness", "Eloquence", "Firmness", "Magnanimity",
            "Voluntariness", "Amiability", "Modesty", "Vitality", "Diligence",
            "Helpfulness", "Empathy", "Radiance", "Decency", "Nobility",
            "Fortitude", "Cordiality", "Inspiration", "Understanding",
            "Appreciation", "Good humor", "Cooperation", "Understanding",
            "Patience", "Sharing"
        ]
        self.goodwords = [
            "Hate", "Sadness", "Ingratitude", "Conflict", "Failure", "Illness",
            "Dissonance", "Selfishness", "Disrespect", "Adversity", "Apathy",
            "Sorrow", "Fear", "Despair", "Turmoil", "Pessimism", "Doubt",
            "Stagnation", "Decline", "Defeat", "Indifference", "Ruthlessness",
            "Discord", "Deceit", "Dishonesty", "Betrayal", "Isolation", "Ignorance",
            "Inertia", "Poverty", "Desperation", "Exclusion", "Confrontation",
            "Imbalance", "Poverty", "Demotivation", "Stagnation", "Misunderstanding",
            "Silence", "Impatience", "Stagnation", "Stupidity", "Demotivation",
            "Indifference", "Harshness", "Destruction", "Dependence", "Insecurity",
            "Dullness", "Inauthenticity", "Low self-esteem", "Selfishness", "Hostility",
            "Exhaustion", "Distrust", "Neglect", "Complexity", "Obscurity",
            "Enslavement", "Pessimism", "Self-doubt", "Cruelty", "Drain",
            "Negativity", "Insensitivity", "Rigidity", "Petty", "Ingratitude",
            "Pessimism", "Disloyalty", "Boorishness", "Presumption", "Egoism",
            "Ostentation", "Conceit", "Arrogance", "Depravity", "Mediocrity",
            "Dishonor", "Frailty", "Sloth", "Apathy", "Indolence", "Negligence",
            "Cowardice", "Dejection", "Lethargy", "Ineptness", "Disarray",
            "Disorganization", "Humiliation", "Insolence", "Procrastination",
            "Intolerance", "Disruption", "Stubbornness", "Inhibition",
            "Rudeness", "Indignity"
        ]
        self.n = 420
