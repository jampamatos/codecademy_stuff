using System;

public class Node<T>
{
    public T? Value { get; set; }
    public Node<T>? NextNode { get; set; }

    public Node(T value, Node<T>? nextNode = null)
    {
        Value = value;
        NextNode = nextNode;
    }
}


public class LinkedList<T>
{
    private Node<T>? headNode;

    public LinkedList(T value = default(T))
    {
        if (!Equals(value, default(T)))
        {
            headNode = new Node<T>(value);
        }
        else
        {
            headNode = null;
        }
    }

    public void InsertBeginning(T newValue)
    {
        Node<T> newNode = new Node<T>(newValue, headNode);
        headNode = newNode;
    }

    public string StringifyList()
    {
        string stringList = "";
        Node<T>? currentNode = headNode;
        while (currentNode != null)
        {
            if (!Equals(currentNode.Value, default(T)))
            {
                stringList += currentNode.Value?.ToString() + "\n";
            }
            currentNode = currentNode.NextNode;
        }
        return stringList;
    }

    public void RemoveNode(T valueToRemove)
    {
        Node<T>? currentNode = headNode;

        if (currentNode != null && Equals(currentNode.Value, valueToRemove))
        {
            headNode = currentNode.NextNode;
            return;
        }

        while (currentNode != null)
        {
            Node<T>? nextNode = currentNode.NextNode;
            if (nextNode != null && Equals(nextNode.Value, valueToRemove))
            {
                currentNode.NextNode = nextNode.NextNode;
                break;
            }
            else
            {
                currentNode = nextNode;
            }
        }
    }
}


class Program {
    static void Main(string[] args) {
        LinkedList<string> list = new LinkedList<string>();
        list.InsertBeginning("Hello");
        list.InsertBeginning("World");
        list.InsertBeginning("!");
        Console.WriteLine(list.StringifyList());
        list.RemoveNode("World");
        Console.WriteLine(list.StringifyList());
    }
}