import java.util.ArrayList;
public class hw10{
    @FunctionalInterface
    interface MapOp<T> {
        T apply(T ap);
    }
    public static void main(String[] args)
    {
        //Implementation using a lambda function
        ArrayList<Integer> intList = new ArrayList<Integer>();
        intList.add(1);
        intList.add(2);
        intList.add(3);
        MapOp<Integer> funcInt = elm -> elm + 4;
        ArrayList<Integer> mappedListInt = mapNums(intList, funcInt);
        mappedListInt.forEach(elm -> System.out.println(elm));

        //Implementation using decleration of the function interface
        ArrayList<Character> charList = new ArrayList<Character>();
        charList.add('a');
        charList.add('b');
        charList.add('c');
        MapOp<Character> funcChar = new MapOp<Character>(){
            @Override
            public Character apply(Character elm){
                return new Character((char)(elm.charValue()+1));
            }
        };
        ArrayList<Character> mappedListChar = mapChars(charList, funcChar);
        for(Character elm : mappedListChar)
        {
            System.out.println(elm);
        }
    }

    public static ArrayList<Character> mapChars(ArrayList<Character> list, MapOp<Character> func)
    {
        ArrayList<Character> retList = new ArrayList<Character>();
        for(int i = 0; i < list.size();i++){
            retList.add(func.apply(list.get(i)));
        }
        return retList;
    }

    public static ArrayList<Integer> mapNums(ArrayList<Integer> list, MapOp<Integer> func)
    {
        ArrayList<Integer> retList = new ArrayList<Integer>();
        for(int i = 0; i < list.size();i++){
            retList.add(func.apply(list.get(i)));
        }
        return retList;
    }
}