import React, { useEffect, useState } from 'react'
import { FoodplanerItem, Meal } from '../Datatypes/Meal'
import AddMealButton from './AddMealButton';
import MealCard from './MealCard';
import { Draggable, Droppable } from 'react-beautiful-dnd';
import { MealService } from '../Endpoints/MealService';

interface Props {
    listId: string,
    listType?: string,
    internalScroll?: boolean,
    isCombinedEnabled?: boolean,
    isMealList?: boolean,
};

function MealList({ listId, listType, internalScroll }: Props) {
    const [meals, setMeals] = useState<Meal[]>([])

    useEffect(() => {
        async function fetchData() {
            try {
                const data: Meal[] = await MealService.getAllMeals();
                setMeals(data)
            } catch (error) {
                console.error('Error fetching planer:', error);
            }
        }
        fetchData()
    }, [])

    return (
        <div className='flex w-full flex-col items-center justify-start'>

            <h2>MealList</h2>

            <Droppable
                droppableId={listId}
                type={listType}
                direction="vertical"
                isCombineEnabled={false}
            >
                {dropProvided => {
                    return (
                        <div
                            className='w-full'
                            ref={dropProvided.innerRef}
                            {...dropProvided.droppableProps}>
                            {meals.map((food, index) => (
                                <Draggable
                                    key={listId + "-" + food.id + "-" + index}
                                    draggableId={listId + "-" + food.id + "-" + index}
                                    index={index}>
                                    {
                                        dragProvided => {
                                            return (
                                                <div
                                                    {...dragProvided.dragHandleProps}
                                                    {...dragProvided.draggableProps}
                                                    ref={dragProvided.innerRef}>
                                                    <MealCard mealID={food.id + ""} index={index} />

                                                </div>
                                            )
                                        }
                                    }
                                </Draggable>
                            ))}
                            <AddMealButton title='Remove' />

                            {dropProvided.placeholder}
                        </div>
                    )
                }}
            </Droppable>

        </div>

    )
}

export default MealList