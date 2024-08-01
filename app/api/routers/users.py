from fastapi import APIRouter

router = APIRouter()


# @router.get(
#     "/",
#     dependencies=[Depends(get_current_active_superuser)],
#     response_model=UsersPublic,
# )
# def read_users(session: SessionDep, skip: int = 0, limit: int = 100) -> Any:
#     """
#     Retrieve users.
#     """
#
#     count_statement = select(func.count()).select_from(User)
#     count = session.exec(count_statement).one()
#
#     statement = select(User).offset(skip).limit(limit)
#     users = session.exec(statement).all()
#
#     return UsersPublic(data=users, count=count)
#
# @router.post(
#     "/", dependencies=[Depends(get_current_active_superuser)], response_model=UserPublic
# )
# def create_user(*, session: SessionDep, user_in: UserCreate) -> Any:
#     """
#     Create new user.
#     """
#     user = crud.get_user_by_email(session=session, email=user_in.email)
#     if user:
#         raise HTTPException(
#             status_code=400,
#             detail="The user with this email already exists in the system.",
#         )
#
#     user = crud.create_user(session=session, user_create=user_in)
#     if settings.emails_enabled and user_in.email:
#         email_data = generate_new_account_email(
#             email_to=user_in.email, username=user_in.email, password=user_in.password
#         )
#         send_email(
#             email_to=user_in.email,
#             subject=email_data.subject,
#             html_content=email_data.html_content,
#         )
#     return user
#
#
# @router.post("/signup", response_model=UserPublic)
# def register_user(session: SessionDep, user_in: UserRegister) -> Any:
#     """
#     Create new user without the need to be logged in.
#     """
#     if not settings.USERS_OPEN_REGISTRATION:
#         raise HTTPException(
#             status_code=403,
#             detail="Open user registration is forbidden on this server",
#         )
#     user = crud.get_user_by_email(session=session, email=user_in.email)
#     if user:
#         raise HTTPException(
#             status_code=400,
#             detail="The user with this email already exists in the system",
#         )
#     user_create = UserCreate.model_validate(user_in)
#     user = crud.create_user(session=session, user_create=user_create)
#     return user
#
#
# @router.delete("/{user_id}", dependencies=[Depends(get_current_active_superuser)])
# def delete_user(
#     session: SessionDep, current_user: CurrentUser, user_id: int
# ) -> Message:
#     """
#     Delete a user.
#     """
#     user = session.get(User, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     if user == current_user:
#         raise HTTPException(
#             status_code=403, detail="Super users are not allowed to delete themselves"
#         )
#     statement = delete(Item).where(col(Item.owner_id) == user_id)
#     session.exec(statement)  # type: ignore
#     session.delete(user)
#     session.commit()
#     return Message(message="User deleted successfully")
