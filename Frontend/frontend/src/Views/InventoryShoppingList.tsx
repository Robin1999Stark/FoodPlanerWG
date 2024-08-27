import { useEffect, useState } from "react";
import { ShoppingList } from "../Datatypes/ShoppingList";
import InventoryListView from "./InventoryListView"
import ShoppingListView from "./ShoppingListView"
import { PiWarehouseDuotone } from "react-icons/pi";
import { RiShoppingCartLine } from "react-icons/ri";

function InventoryShoppingList() {
    const SIZE_MOBILE = 700;

    const [shoppingList, setShoppingList] = useState<ShoppingList>();
    const [toggleShoppingList, setToggleShoppingList] = useState<boolean>(true);
    const [windowSize, setWindowSize] = useState({
        width: window.innerWidth,
        height: window.innerHeight,
    });
    const handleResize = () => {
        setWindowSize({
            width: window.innerWidth,
            height: window.innerHeight,
        });
    }
    useEffect(() => {
        window.addEventListener('resize', handleResize);
        return () => {
            window.removeEventListener('resize', handleResize);
        };
    }, []);

    if (windowSize.width > SIZE_MOBILE) {
        return (
            <>
                <section className='flex flex-row pt-4 h-full justify-start items-start'>
                    <section className='flex-1 pl-6 pr-4 h-full'>
                        {<ShoppingListView shoppingList={shoppingList} setShoppingList={setShoppingList} />}
                    </section>
                    <section className='flex-1 pr-6 pl-4 h-full'>
                        <InventoryListView />
                    </section>
                </section>
            </>
        )
    } else {
        return (
            <>
                <section className='flex flex-row pt-4 h-full justify-start items-start'>
                    {
                        toggleShoppingList ? <section className='flex-1 pl-6 pr-4 h-[95%]'>
                            {<ShoppingListView shoppingList={shoppingList} setShoppingList={setShoppingList} />}
                        </section> :
                            <section className='flex-1 pr-6 pl-4 h-[95%]'>
                                <InventoryListView />
                            </section>
                    }
                </section>
                <span className='absolute left-0 right-0 py-1 bottom-20 bg-white'>
                    <ul className='flex flex-row justify-between mx-4 items-center bg-[#E8E9EB] rounded-full p-1'>
                        <li
                            onClick={() => setToggleShoppingList(true)}
                            className={`w-full flex flex-row py-1 cursor-pointer justify-center items-center ${toggleShoppingList ? 'bg-[#004A41] text-white font-bold' : 'text-[#011413]'} rounded-full items-center`}>
                            <RiShoppingCartLine className='size-5 mr-2' />
                            <p className='text-sm'>
                                Einkaufsliste
                            </p>
                        </li>
                        <li
                            onClick={() => setToggleShoppingList(false)}
                            className={`w-full flex flex-row py-1 cursor-pointer justify-center items-center ${!toggleShoppingList ? 'bg-[#004A41] text-white font-bold' : 'text-[#011413]'} rounded-full items-center`}>
                            <PiWarehouseDuotone className='size-5 mr-2' />
                            <p className='text-sm'>
                                Bestandsliste
                            </p>
                        </li>
                    </ul>
                </span>
            </>

        )
    }


}

export default InventoryShoppingList 