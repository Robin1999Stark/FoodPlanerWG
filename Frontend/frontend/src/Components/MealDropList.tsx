import { useEffect, useState } from 'react';
import { Draggable, Droppable } from 'react-beautiful-dnd';
import MealDragElement from './MealDragElement';
import { Weekday } from '../Datatypes/Weekday';
import DropMealPlaceholder from './DropMealPlaceholder';
import { FoodplanerItem } from '../Datatypes/FoodPlaner';
import { FaCheckCircle } from 'react-icons/fa';

interface Props {
    planerItem: FoodplanerItem,
    listId: string,
    listType?: string,
    internalScroll?: boolean,
    isCombinedEnabled?: boolean,
    onRemoveMeal?: (planerDate: Date, mealId: number) => void;
    onMoveMeal?: (from: Date, to: Date, mealId: number) => void;
    onAddMeal?: (to: Date, mealId: number) => void;
}

function MealDropList({ listId, listType, planerItem, onRemoveMeal, onMoveMeal }: Props) {
    const [isEmpty, setIsEmpty] = useState<boolean>(planerItem.meals.length === 0);

    useEffect(() => {
        setIsEmpty(planerItem.meals.length === 0);
    }, [planerItem.meals]);

    const displayTitle = (isEmpty: boolean) => {
        const isToday = new Date(Date.now()).getDate() === new Date(planerItem.date).getDate()
        return (
            <span className='flex select-none flex-row justify-start items-center w-full rounded-md my-4'>
                <FaCheckCircle className={`${isEmpty ? 'text-slate-200' : 'text-[#046865]'} size-4 mr-2`} />
                <h2 className={isToday ? isEmpty ? 'text-[#F96E46] text-sm font-bold' : 'text-[#046865] text-sm font-bold' : 'text-[#011413] text-sm font-semibold'}>
                    {planerItem.date instanceof Date ? Weekday[planerItem.date.getDay()] : Weekday[new Date(planerItem.date).getDay()]}
                    {", " + new Date(planerItem.date).getDate() + "." + (new Date(planerItem.date).getMonth() + 1) + "." + (new Date(planerItem.date).getFullYear())}
                </h2>
            </span>
        )
    }
    const displayPlaceholder = () => {
        if (isEmpty)
            return <DropMealPlaceholder />;
        return null;
    }

    return (
        <span className={'flex w-full flex-col items-start justify-start'} >

            {displayTitle(isEmpty)}

            <Droppable
                droppableId={listId}
                type={listType}
                direction="vertical"
                isCombineEnabled={false}
            >
                {(dropProvided, snapshot) => {
                    return (
                        <ul
                            style={{ scrollbarWidth: 'none' }}
                            className={snapshot.isDraggingOver ? 'w-full min-h-4 border-2 border-dotted border-[#046865]' : 'w-full min-h-4 border-2 border-[#00000000]'}
                            ref={dropProvided.innerRef}
                            {...dropProvided.droppableProps}>
                            {planerItem.meals.map((food, index) => (
                                <Draggable
                                    key={listId + "-" + food + "-" + index}
                                    draggableId={listId + "-" + food + "-" + index}
                                    index={index}>
                                    {
                                        (dragProvided, snapshot) => {
                                            return (
                                                <MealDragElement
                                                    onRemoveMeal={onRemoveMeal}
                                                    onMoveMeal={onMoveMeal}
                                                    mealID={food}
                                                    date={planerItem.date}
                                                    dragProvided={dragProvided}
                                                    snapshot={snapshot}
                                                    index={index} />
                                            )
                                        }
                                    }
                                </Draggable>
                            ))}
                            {isEmpty && displayPlaceholder()}
                            {dropProvided.placeholder}
                        </ul>
                    )
                }}
            </Droppable>
        </span>
    )
}

export default MealDropList