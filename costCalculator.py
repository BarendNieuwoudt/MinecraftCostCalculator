import json, sys

def loadRecipe(item):
	try:
		with open(f'recipes/{item}.json', 'r') as f:
			return json.load(f)
	except:
		return None

# Print the costs for an item
def printCostsForItem(costs, item, amount, spacer):
	print(f"{spacer}{item} : {costs[item]} = {str(round((costs[item]/64)*amount, 2))} stacks")
	
# Add an amount of ingredient to the costs
# If an ingredient needs to be crafted, its ingredients will be considered
def addIngredients(item, costs, amount, recipe, spacer):
	print(spacer + str(item))
	
	if recipe is None:
		# this doesnt require further crafting
		if item in costs:
			costs[item] = costs[item] + amount
			# This item's ingredients, is only the item itself
			printCostsForItem({"redstone_dust":amount}, item, 1, spacer + '-')
		else:
			costs[item] = float(recipe[item]) * amount
			printCostsForItem(costs, item, amount, spacer + '-')
		return
	
	# This item needs to be crafted
	for ingredient in recipe:
		if loadRecipe(ingredient) is None:
			# this doesnt require further crafting
			if ingredient in costs:
				costs[ingredient] = costs[ingredient] + (float(recipe[ingredient]) * amount)
				printCostsForItem(recipe, ingredient, amount, spacer + '-')
			else:
				costs[ingredient] = float(recipe[ingredient]) * amount
				printCostsForItem(recipe, ingredient, amount, spacer + '-')
		else:
			# need to consider this ingredient's ingredients
			addIngredients(ingredient, costs, amount*(float(recipe[ingredient])), loadRecipe(ingredient), spacer + '-')
			

# Print the costs after all the items, 
# and their ingredients have been considered
def printCosts(costs):
	print('\nFinal Costs')
	for item in costs.keys():
		printCostsForItem(costs, item, 1, '')

if __name__ == "__main__":
	# called like
	# python costCalculator item:amount,item:amount,...
	# python costCalculator.py hopper:258,barrel:176,redstone_dust:176
	
	costs = {}
	
	for item in sys.argv[1].strip().split(','):
		# Call the first time, with the recipe already loaded
		addIngredients(item.split(':')[0], costs, float(item.split(':')[1]), loadRecipe(item.split(':')[0]), '')
			
	printCosts(costs)