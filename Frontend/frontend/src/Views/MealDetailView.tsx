import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { MealService } from '../Endpoints/MealService'
import { Link } from 'react-router-dom'
import { MealIngredientService } from '../Endpoints/MealIngredientService'
import PlaceholderMealImage from '../Components/PlaceholderMealImage'
import URLify from '../Helperfunctions/urlify'
import { LuClock } from "react-icons/lu";
import { PlanerService } from '../Endpoints/PlanerService'
import { IngredientAmount } from '../Datatypes/Ingredient'
import { Meal, MealTags } from '../Datatypes/Meal'
import { TagService } from '../Endpoints/TagService'
import Tag from '../Components/Tag'
import { Menu, MenuButton, MenuItem } from '@szhsin/react-menu'
import { IoIosMore } from 'react-icons/io'

function MealDetailView() {
    const navigate = useNavigate();
    const { mealID } = useParams();

    const [meal, setMeal] = useState<Meal>()
    const [_error, setError] = useState<string>("")
    const [mealIngredients, setMealIngredients] = useState<IngredientAmount[]>([])
    const [isPlanned, setIsPlanned] = useState<PlanerService.IsPlannedResponse>();
    const [tags, setTags] = useState<MealTags>();

    function displayIsPlanned() {
        if (isPlanned && isPlanned.isPlanned) {
            return <label aria-label='planned for' className='text-[#046865] font-bold text-sm'>{'geplant: ' + new Date(isPlanned.plannedDate!).toLocaleDateString()}</label>
        } else {
            return <></>
        }
    }
    useEffect(() => {

        async function fetchTags(id: string) {
            try {
                const response = await TagService.getAllTagsFromMeal(Number(id));
                response ? setTags(response) : setError("No Meal Found");
            } catch (error) {
                setError("Error while fetching Tags occured");
            }
        }

        async function fetchMeal() {
            try {
                const response = await MealService.getMeal(mealID!)
                response ? setMeal(response) : setError("Error occured while fetching Meal")
            } catch (e) {
                console.log(e)
            }
        }


        async function fetchMealIngredients() {
            try {
                const response = await MealIngredientService.getAllMealIngredients(Number(mealID!))
                response ? setMealIngredients(response) : setMealIngredients([])
                console.log(mealIngredients)
            } catch (e) {
                console.log(e)
            }
        }

        async function checkIsPlanned(mealId: string) {
            try {
                const response = await PlanerService.isPlanned(Number(mealId));
                return response;
            } catch (error) {
                console.error(error)
            }
            return null;
        }
        async function fetchAllData() {
            if (mealID === undefined) return;
            fetchMeal();
            fetchTags(mealID);
            fetchMealIngredients();
            const planned = await checkIsPlanned(mealID!);
            if (!planned) return;
            setIsPlanned(planned);
        }
        fetchAllData()

    }, [])

    return (
        <>
            <section className='w-full absolute left-[50%] translate-x-[-50%] px-8 mt-8 max-w-[70rem]'>
                <span className='flex flex-row justify-between items-center'>
                    <span className='flex flex-row justify-start items-center'>
                        <h1 className='font-semibold text-[#011413] text-2xl mx-2'>
                            {meal?.title}
                        </h1>
                        <sup>
                            {displayIsPlanned()}
                        </sup>
                    </span>

                    <Menu menuButton={<MenuButton><IoIosMore className='size-5 mr-4 text-[#011413]' /></MenuButton>} transition>
                        <MenuItem onClick={() => navigate(`tags`)}>Tags Anpassen</MenuItem>
                        <MenuItem onClick={() => navigate(`edit`)}>Gericht Anpassen</MenuItem>
                    </Menu>
                </span>
                <hr className='my-4' />
                <span className='w-full flex flex-row justify-between items-start'>
                    <ul className='w-full flex flex-1 flex-row justify-start h-full flex-wrap items-center'>
                        {tags?.tags.map(tag => (
                            <li className='mr-1'>
                                <Tag title={tag} />

                            </li>
                        ))}

                    </ul>
                    <div className='ml-5 flex flex-row truncate  justify-end items-center'>
                        <LuClock className='size-4' />
                        <p className='ml-2 font-semibold'>
                            {meal?.duration} Minuten
                        </p>
                    </div>
                </span>

                <hr className='mt-4 mb-8' />
                <section className='flex flex-wrap w-full'>
                    <span className='w-full max-w-[22rem]'>
                        <PlaceholderMealImage rounded border='full' />
                    </span>
                    <div className="w-full pl-20 flex-1 md:w-1/2 flex flex-col justify-between text-[#011413] h-full lg:w-1/2 xl:w-1/2 p-4 min-w-[200px]">
                        <blockquote className='mb-6'>
                            {meal?.description &&
                                <URLify text={meal?.description} />
                            }

                        </blockquote>
                        <div className='py-3 min-w-[200px]'>
                            <h2 className='truncate my-2 text-lg font-bold'>
                                Zutaten:
                            </h2>
                            {
                                mealIngredients ?
                                    <ul className='h-full my-2'>
                                        {mealIngredients?.map(ingredient => (
                                            <li key={ingredient.ingredient + Math.random()} className='py-1 w-full flex flex-row text-base font-semibold justify-between'>
                                                <Link to={`/ingredients/${ingredient.ingredient}`}>{ingredient.ingredient}</Link>
                                                {ingredient.amount + " " + ingredient.unit + " "}

                                            </li>))}
                                    </ul> : <h2>Loading ...</h2>
                            }
                        </div>
                        <article className='my-6 w-full'>
                            <h2 className='truncate my-2 text-lg font-bold'>
                                Zubereitung:
                            </h2>
                            <p className='text-base text-start font-medium text-[#011413] text'>
                                {meal?.preparation ? <URLify text={meal.preparation} /> : "No Preparation found"}
                            </p>
                        </article>


                    </div>
                </section>

            </section>

        </>
    )
}

export default MealDetailView