from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    """Test creating a user in the database."""
    user = User(
        username='guidurbano',
        email='guidurbano@gmail.com',
        password='password123',
    )

    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'guidurbano@gmail.com')

    )

    assert result.username == 'guidurbano'
    assert user.id == 1
