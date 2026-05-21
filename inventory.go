package main

import (
	"errors"
	"fmt"
)

type Item struct {
	ID       int
	Name     string
	Quantity int
	Price    float64
}

type Inventory struct {
	items  map[int]*Item
	nextID int
}

func NewInventory() *Inventory {
	return &Inventory{items: make(map[int]*Item), nextID: 1}
}

func (inv *Inventory) AddItem(name string, qty int, price float64) *Item {
	item := &Item{
		ID:       inv.nextID,
		Name:     name,
		Quantity: qty,
		Price:    price,
	}
	inv.items[inv.nextID] = item
	inv.nextID++
	return item
}

func (inv *Inventory) Restock(id, qty int) error {
	item, ok := inv.items[id]
	if !ok {
		return errors.New("item not found")
	}
	if qty <= 0 {
		return errors.New("quantity must be positive")
	}
	item.Quantity += qty
	return nil
}

func (inv *Inventory) Sell(id, qty int) error {
	item, ok := inv.items[id]
	if !ok {
		return errors.New("item not found")
	}
	if qty > item.Quantity {
		return fmt.Errorf("insufficient stock: have %d, need %d", item.Quantity, qty)
	}
	item.Quantity -= qty
	return nil
}

func (inv *Inventory) TotalValue() float64 {
	total := 0.0
	for _, item := range inv.items {
		total += float64(item.Quantity) * item.Price
	}
	return total
}

func (inv *Inventory) LowStock(threshold int) []*Item {
	var result []*Item
	for _, item := range inv.items {
		if item.Quantity <= threshold {
			result = append(result, item)
		}
	}
	return result
}

func main() {
	inv := NewInventory()
	inv.AddItem("Widget A", 100, 2.99)
	inv.AddItem("Gadget B", 5, 49.99)
	inv.AddItem("Doohickey C", 50, 9.99)

	inv.Sell(1, 20)
	inv.Restock(2, 15)

	fmt.Printf("Total inventory value: $%.2f\n", inv.TotalValue())

	low := inv.LowStock(10)
	fmt.Printf("Low stock items (%d):\n", len(low))
	for _, item := range low {
		fmt.Printf("  - %s: %d units\n", item.Name, item.Quantity)
	}
}
