import recipes
from sys import argv

if __name__ == '__main__':
    
    if len(argv) > 1:
        
        ingredients = argv[1:]
        ingredients = [ingredient.rstrip(',') for ingredient in ingredients]
        
        pred_class = recipes.Predict(ingredients)
        predict = pred_class.model_predict()
        
        calc_nutrions = recipes.CalculateNutritionFacts(ingredients)
        nutrions = calc_nutrions.nutrition_facts()
        
        similar_recipies = recipes.SimilarRecipes(ingredients)
        recipies = similar_recipies.get_recipe()
        
        print('\n', '-' * 30, sep='')
        print('I. OUR FORECAST:\n')
        print(predict, '\n')
        print('II. NUTRITION FACTS:\n')
        print(nutrions, '\n')
        print('III. TOP-3 SIMILAR RECIPES:\n')
        print(recipies)
        print('-' * 30, '\n')
        
    else:
        print("Uncorrect input")
    