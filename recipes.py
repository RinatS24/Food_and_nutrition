import joblib
import pandas as pd

class Predict:
    
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.model = joblib.load('bagging_clf.pkl')
        
    def to_features(self):
        
        features = pd.read_csv('features.csv')
        
        for ingredient in self.ingredients:
            if ingredient in features.columns:
                features[ingredient] = 1
            
        return features
    
    def model_predict(self):
        
        features = self.to_features()
        
        y_pred = self.model.predict(features)[0]
        
        answer = ''
        if y_pred == 1:
            answer = "You might find it delicious, and we wholeheartedly agree! This \
combination of ingredients is sure to create a fantastic dish that everyone will enjoy."

        elif y_pred == 2:
            answer = "You might find it acceptable, but we believe that the combination \
of those ingredients doesn't quite hit the mark for a memorable dish."

        elif y_pred == 3:
            answer = "You might find it tasty, but in our opinion, it is a bad idea to have a \
dish with that list of ingredients."
            
        return answer
    
class CalculateNutritionFacts:
    
    def __init__(self,ingredients):
        self.ingredients = ingredients

    def nutrition_facts(self):
        
        df = pd.read_csv('new_nutrients.csv', index_col=0)
        descriptions = []  

        for ingredient in self.ingredients:
            if ingredient in df.index:
                row = df.iloc[df.index.get_loc(ingredient), :-3]
                description = [ingredient.capitalize()]

                for nutrient, value in row.items():
                    if value != 0:
                        description.append(f"{nutrient} - {int(value)}% of Daily Value")
                if len(description) == 1:
                    description.append('- ...')

                descriptions.append("\n".join(description))
            
        if len(description) == 1:
            description.append('- ...')
                
        return "\n\n".join(descriptions)

class SimilarRecipes:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def get_recipe(self):
        
        df = pd.read_csv('new_nutrients.csv', index_col=0)
        
        recipes = []
        
        for ingredient in self.ingredients:
            if ingredient in df.index:
                row = df.loc[ingredient, df.columns[-3:]].values
                row = list(map(str, row))
                row[1] = '- ' + row[1]
                row[1] = 'rating: ' + row[1]
                row[2] = 'URL: ' + row[2]
                row = ', '.join(row)
                recipes.append(row)
                
        if len(recipes) < 3:
            recipes.append('-...')
            
        return "\n".join(recipes[:3])
        