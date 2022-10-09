import collections
import unittest
import app2 as app

class TestMyShopApp(unittest.TestCase):
  def setUp(self):
    self.app = app
  
  def test_entered_product(self):
    products = ["Iphone", "Laptop", "Computer", "TV", "Mouse", "Keyboard"]
    self.assertTrue(app.checkEnteredType('laptop', products))
    self.assertFalse(app.checkEnteredType('tablet', products))
  
  def test_entered_amount(self):
    self.assertTrue(app.checkEnteredAmount('8'))
    self.assertFalse(app.checkEnteredAmount('Hello'))

  def test_create_description(self):
    self.assertEqual(app.createDescription('Laptop', 4), '4 laptops')
    self.assertEqual(app.createDescription('TV', 23), '23 tvs')

  def test_add_order(self):
    table = collections.deque()
    table.append({ 'type': "Laptop", 'amount': 2, 'descr': '2 laptops' })

    self.assertEqual(len(app.addOrderToTable(table, 'Keyboard', 4)), 2)

  def tearDown(self):
    pass

if __name__ == '__main__':
  unittest.main()
