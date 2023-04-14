from django.contrib.auth import get_user_model

User = get_user_model()


class UserService:
    """
        Collection of methods to interact with the User model
    """

    @staticmethod
    def create_user(*, email: str, password: str, username: str) -> User:
        """
            Create a user in the system
        """
        user = self.User.objects.create(email=email, username=username)
        user.set_password(password)

        return user

    @staticmethod
    def update_user(*, user_id, **kwargs) -> bool:
        """
            Updates a user in the system, and returns True if the user was updated
        """
        pass
