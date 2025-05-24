import ecommerce.shipping #1
from ecommerce import shipping #2
from ecommerce.shipping import * #3 import all functions
from ecommerce.shipping import calc_shipping #3 specific import

ecommerce.shipping.calc_shipping() #1
shipping.calc_shipping() #2
calc_shipping() #3